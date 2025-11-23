#!/usr/bin/env python3
"""
Dashboard Web Flask - Interface de Gestion du Lab
"""

from flask import Flask, render_template_string, jsonify, request
import os
import json
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_FILE = r"C:\Lab\AppLockerbypassLab\scripts\lab_results.db"

# ═══════════════════════════════════════════════════════
# DATABASE SETUP
# ═══════════════════════════════════════════════════════

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS test_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            payload_name TEXT,
            technique TEXT,
            status TEXT,
            applocker_blocked INTEGER,
            sysmon_events INTEGER,
            notes TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            created_at TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS campaign_tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_id INTEGER,
            binary TEXT,
            technique TEXT,
            path TEXT,
            status TEXT,
            FOREIGN KEY(campaign_id) REFERENCES campaigns(id)
        )
    """)

    conn.commit()
    conn.close()


init_db()

# ═══════════════════════════════════════════════════════
# TEMPLATE HTML
# ═══════════════════════════════════════════════════════

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AppLocker Bypass Lab Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        header {
            background: #2d3748;
            color: white;
            padding: 30px;
            text-align: center;
        }
        header h1 { font-size: 2.5em; margin-bottom: 10px; }
        header p { opacity: 0.8; }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f7fafc;
        }
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stat-card h3 { color: #718096; font-size: 0.9em; margin-bottom: 10px; }
        .stat-card .value { font-size: 2.5em; font-weight: bold; color: #2d3748; }
        .stat-card.success .value { color: #48bb78; }
        .stat-card.danger .value { color: #f56565; }
        .stat-card.warning .value { color: #ed8936; }
        
        .controls {
            padding: 30px;
            border-bottom: 1px solid #e2e8f0;
        }
        .btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1em;
            margin-right: 10px;
            transition: all 0.3s;
        }
        .btn:hover { background: #5a67d8; transform: translateY(-2px); }
        .btn.danger { background: #f56565; }
        .btn.danger:hover { background: #e53e3e; }
        
        .results {
            padding: 30px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background: #2d3748;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }
        td {
            padding: 15px;
            border-bottom: 1px solid #e2e8f0;
        }
        tr:hover { background: #f7fafc; }
        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: 600;
        }
        .badge.success { background: #c6f6d5; color: #22543d; }
        .badge.blocked { background: #fed7d7; color: #742a2a; }
        .badge.partial { background: #feebc8; color: #7c2d12; }
        
        .technique-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
            padding: 30px;
            background: #f7fafc;
        }
        .technique-item {
            background: white;
            padding: 15px;
            border-radius: 6px;
            border-left: 4px solid #667eea;
            cursor: pointer;
            transition: all 0.3s;
        }
        .technique-item:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🛡️ AppLocker Bypass Lab</h1>
            <p>Framework d'Automatisation de Tests LOLBAS</p>
        </header>
        
        <div class="stats">
            <div class="stat-card success">
                <h3>BYPASSES RÉUSSIS</h3>
                <div class="value" id="success-count">0</div>
            </div>
            <div class="stat-card danger">
                <h3>BLOQUÉS</h3>
                <div class="value" id="blocked-count">0</div>
            </div>
            <div class="stat-card warning">
                <h3>TESTS TOTAUX</h3>
                <div class="value" id="total-count">0</div>
            </div>
            <div class="stat-card">
                <h3>TAUX DE SUCCÈS</h3>
                <div class="value" id="success-rate">0%</div>
            </div>
        </div>
        
        <div class="controls">
            <button class="btn" onclick="runTests()">▶️ Lancer Tests</button>
            <button class="btn" onclick="generatePayloads()">🔧 Générer Payloads</button>
            <button class="btn" onclick="refreshResults()">🔄 Actualiser</button>
            <button class="btn danger" onclick="clearResults()">🗑️ Effacer Résultats</button>
        </div>
        
        <div class="results">
            <h2 style="margin-bottom: 20px;">📊 Résultats des Tests</h2>
            <table id="results-table">
                <thead>
                    <tr>
                        <th>Date/Heure</th>
                        <th>Payload</th>
                        <th>Technique</th>
                        <th>Statut</th>
                        <th>Événements</th>
                        <th>Notes</th>
                    </tr>
                </thead>
                <tbody id="results-body">
                    <tr><td colspan="6" style="text-align:center;">Aucun résultat disponible</td></tr>
                </tbody>
            </table>
        </div>
        
        <div style="padding: 30px;">
            <h2 style="margin-bottom: 20px;">🎯 Techniques LOLBAS Disponibles</h2>
            <div class="technique-list">
                <div class="technique-item" onclick="showTechnique('mshta')">
                    <strong>MSHTA.exe</strong><br>
                    <small>HTML Application</small>
                </div>
                <div class="technique-item" onclick="showTechnique('regsvr32')">
                    <strong>REGSVR32.exe</strong><br>
                    <small>SCT Scripts</small>
                </div>
                <div class="technique-item" onclick="showTechnique('rundll32')">
                    <strong>RUNDLL32.exe</strong><br>
                    <small>DLL Loading</small>
                </div>
                <div class="technique-item" onclick="showTechnique('msbuild')">
                    <strong>MSBUILD.exe</strong><br>
                    <small>XML Projects</small>
                </div>
                <div class="technique-item" onclick="showTechnique('installutil')">
                    <strong>INSTALLUTIL.exe</strong><br>
                    <small>.NET Installer</small>
                </div>
                <div class="technique-item" onclick="showTechnique('wmic')">
                    <strong>WMIC.exe</strong><br>
                    <small>XSL Execution</small>
                </div>
                <div class="technique-item" onclick="showTechnique('cscript')">
                    <strong>CSCRIPT.exe</strong><br>
                    <small>VBS/JS Scripts</small>
                </div>
                <div class="technique-item" onclick="showTechnique('pubprn')">
                    <strong>PUBPRN.vbs</strong><br>
                    <small>Printer Script</small>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        function refreshResults() {
            fetch('/api/results')
                .then(r => r.json())
                .then(data => {
                    updateStats(data);
                    updateTable(data);
                });
        }
        
        function updateStats(data) {
            const success = data.filter(r => r.status === 'bypass').length;
            const blocked = data.filter(r => r.status === 'blocked').length;
            const total = data.length;
            const rate = total > 0 ? Math.round((success/total)*100) : 0;
            
            document.getElementById('success-count').textContent = success;
            document.getElementById('blocked-count').textContent = blocked;
            document.getElementById('total-count').textContent = total;
            document.getElementById('success-rate').textContent = rate + '%';
        }
        
        function updateTable(data) {
            const tbody = document.getElementById('results-body');
            if (data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;">Aucun résultat</td></tr>';
                return;
            }
            
            tbody.innerHTML = data.map(r => `
                <tr>
                    <td>${r.timestamp}</td>
                    <td><code>${r.payload_name}</code></td>
                    <td>${r.technique}</td>
                    <td><span class="badge ${r.status === 'bypass' ? 'success' : 'blocked'}">${r.status.toUpperCase()}</span></td>
                    <td>${r.sysmon_events} événements Sysmon</td>
                    <td>${r.notes || '-'}</td>
                </tr>
            `).join('');
        }
        
        function runTests() {
            if (confirm('Lancer une campagne de tests complète?')) {
                fetch('/api/run_tests', {method: 'POST'})
                    .then(r => r.json())
                    .then(data => alert(data.message));
            }
        }
        
        function generatePayloads() {
            fetch('/api/generate', {method: 'POST'})
                .then(r => r.json())
                .then(data => alert(data.message));
        }
        
        function clearResults() {
            if (confirm('Effacer tous les résultats?')) {
                fetch('/api/clear', {method: 'POST'})
                    .then(() => refreshResults());
            }
        }
        
        function showTechnique(name) {
            alert('Technique: ' + name.toUpperCase() + '\\nOutils: scripts/generate_payloads.py');
        }
        
        // Auto-refresh every 5 seconds
        setInterval(refreshResults, 5000);
        refreshResults();
    </script>
</body>
</html>
"""

# ═══════════════════════════════════════════════════════
# API ROUTES
# ═══════════════════════════════════════════════════════

@app.route('/')
def index():
    return render_template_string(TEMPLATE)

@app.route("/api/campaign/add_test", methods=["POST"])
def api_campaign_add_test():
    data = request.json

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        INSERT INTO campaign_tests (campaign_id, binary, technique, path, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["campaign_id"],
        data["binary"],
        data["technique"],
        data["path"],
        data["status"]
    ))
    conn.commit()
    conn.close()

    return jsonify({"message": "Test added"})


@app.route("/api/campaign/new", methods=["POST"])
def api_campaign_new():
    data = request.json
    name = data.get("name", "Unnamed Campaign")

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO campaigns (name, created_at) VALUES (?, datetime('now'))", (name,))
    conn.commit()

    campaign_id = c.lastrowid
    conn.close()

    return jsonify({
        "message": "Campaign created",
        "campaign_id": campaign_id,
        "name": name
    })


@app.route("/api/register_test", methods=["POST"])
def register_test():
    data = request.json

    db = sqlite3.connect(DB_FILE)
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO test_results (payload_name, technique, status, applocker_blocked, sysmon_events, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["binary"],
        data["technique"],
        "pending",
        None,
        None,
        f"Path: {data['path']}"
    ))

    db.commit()
    db.close()

    return jsonify({"message": "Test enregistré"})


@app.route('/api/analysis', methods=['GET'])
def analysis():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT technique, status, COUNT(*) FROM test_results GROUP BY technique, status")
    rows = c.fetchall()

    # Préparer les données du rapport
    analysis_data = {}
    for row in rows:
        technique, status, count = row
        if technique not in analysis_data:
            analysis_data[technique] = {'bypass': 0, 'blocked': 0}
        analysis_data[technique][status] = count

    # Calculer la moyenne des événements Sysmon par technique
    c.execute("SELECT technique, AVG(sysmon_events) FROM test_results GROUP BY technique")
    sysmon_avg = {row[0]: row[1] for row in c.fetchall()}

    conn.close()

    # Création du rapport
    report = {
        "analysis": analysis_data,
        "sysmon_avg": sysmon_avg
    }

    return jsonify(report)


@app.route('/api/results')
def get_results():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM test_results ORDER BY timestamp DESC LIMIT 100")
    rows = c.fetchall()
    conn.close()
    
    results = []
    for row in rows:
        results.append({
            'id': row[0],
            'timestamp': row[1],
            'payload_name': row[2],
            'technique': row[3],
            'status': row[4],
            'applocker_blocked': row[5],
            'sysmon_events': row[6],
            'notes': row[7]
        })
    
    return jsonify(results)

@app.route('/api/run_tests', methods=['POST'])
def run_tests():
    # Appeler execute_payloads.ps1
    os.system('powershell -File scripts/execute_payloads.ps1')
    return jsonify({'message': 'Tests lancés en arrière-plan'})

@app.route('/api/generate', methods=['POST'])
def generate():
    os.system('python C:\\Lab\\AppLockerbypassLab\\scripts\\packaging_module.py')
    return jsonify({'message': 'Payloads générés avec succès'})

@app.route('/api/clear', methods=['POST'])
def clear():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM test_results")
    conn.commit()
    conn.close()
    return jsonify({'message': 'Résultats effacés'})

@app.route('/api/add_result', methods=['POST'])
def add_result():
    data = request.json
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        INSERT INTO test_results 
        (timestamp, payload_name, technique, status, applocker_blocked, sysmon_events, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data.get('payload_name'),
        data.get('technique'),
        data.get('status'),
        data.get('applocker_blocked', 0),
        data.get('sysmon_events', 0),
        data.get('notes', '')
    ))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Résultat ajouté'})

if __name__ == '__main__':
    print("\n🌐 Dashboard disponible sur http://localhost:5000")
    print("⚠️  Usage éducatif uniquement - Lab contrôlé\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
