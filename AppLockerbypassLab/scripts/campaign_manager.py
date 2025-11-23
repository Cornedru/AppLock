#!/usr/bin/env python3
"""
Campaign Manager - Orchestration Complète des Tests
Gestion de campagnes de tests avec scoring automatique
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path
import sqlite3

class CampaignManager:
    """Gestionnaire de campagnes de tests automatisées"""
    
    def __init__(self, base_dir="./"):
        self.base_dir = Path(base_dir)
        self.payloads_dir = self.base_dir / "payloads"
        self.logs_dir = self.base_dir / "logs"
        self.campaigns_dir = self.base_dir / "campaigns"
        self.db_file = self.base_dir / "lab_results.db"
        
        # Créer les répertoires nécessaires
        for d in [self.campaigns_dir, self.logs_dir]:
            d.mkdir(exist_ok=True)
        
        self.init_db()
    
    def init_db(self):
        """Initialise la base de données"""
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        
        # Table des campagnes
        c.execute("""
            CREATE TABLE IF NOT EXISTS campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                start_time TEXT,
                end_time TEXT,
                status TEXT,
                total_tests INTEGER DEFAULT 0,
                bypasses INTEGER DEFAULT 0,
                blocked INTEGER DEFAULT 0
            )
        """)
        
        # Table des résultats
        c.execute("""
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id INTEGER,
                timestamp TEXT,
                payload_name TEXT,
                technique TEXT,
                status TEXT,
                applocker_blocked INTEGER,
                sysmon_events INTEGER,
                execution_time REAL,
                notes TEXT,
                FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    # ═══════════════════════════════════════════════════════
    # GESTION DES CAMPAGNES
    # ═══════════════════════════════════════════════════════
    
    def create_campaign(self, name, description=""):
        """Crée une nouvelle campagne de tests"""
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("""
            INSERT INTO campaigns (name, description, start_time, status)
            VALUES (?, ?, ?, 'running')
        """, (name, description, timestamp))
        
        campaign_id = c.lastrowid
        conn.commit()
        conn.close()
        
        # Créer le dossier de campagne
        campaign_dir = self.campaigns_dir / f"campaign_{campaign_id}"
        campaign_dir.mkdir(exist_ok=True)
        
        print(f"[+] Campagne créée: ID={campaign_id}, Nom='{name}'")
        return campaign_id
    
    def end_campaign(self, campaign_id):
        """Termine une campagne et calcule les statistiques"""
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        
        # Calculer les stats
        c.execute("""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN status='bypass' THEN 1 ELSE 0 END) as bypasses,
                SUM(CASE WHEN status='blocked' THEN 1 ELSE 0 END) as blocked
            FROM test_results WHERE campaign_id=?
        """, (campaign_id,))
        
        total, bypasses, blocked = c.fetchone()
        
        # Mettre à jour la campagne
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("""
            UPDATE campaigns 
            SET end_time=?, status='completed', total_tests=?, bypasses=?, blocked=?
            WHERE id=?
        """, (timestamp, total, bypasses, blocked, campaign_id))
        
        conn.commit()
        conn.close()
        
        print(f"[+] Campagne {campaign_id} terminée:")
        print(f"    Total: {total} tests")
        print(f"    Bypasses: {bypasses} ({(bypasses/total*100 if total>0 else 0):.1f}%)")
        print(f"    Bloqués: {blocked} ({(blocked/total*100 if total>0 else 0):.1f}%)")
        
        return {
            'total': total,
            'bypasses': bypasses,
            'blocked': blocked,
            'success_rate': bypasses/total*100 if total>0 else 0
        }
    
    # ═══════════════════════════════════════════════════════
    # EXÉCUTION DE TESTS
    # ═══════════════════════════════════════════════════════
    
    def run_campaign(self, campaign_id, techniques=None):
        """Lance une campagne complète de tests"""
        print(f"\n🚀 Lancement de la campagne {campaign_id}\n")
        
        # Si aucune technique spécifiée, tester toutes
        if techniques is None:
            techniques = [
                "mshta", "regsvr32", "rundll32", "msbuild", 
                "installutil", "wmic", "cscript", "bat", "ps1"
            ]
        
        results = []
        
        for technique in techniques:
            print(f"\n📌 Test de la technique: {technique.upper()}")
            
            technique_dir = self.payloads_dir / technique
            if not technique_dir.exists():
                print(f"   ⚠️  Répertoire {technique} non trouvé")
                continue
            
            # Trouver tous les payloads de cette technique
            payloads = list(technique_dir.glob("*"))
            
            for payload in payloads:
                if payload.suffix in ['.hta', '.sct', '.bat', '.ps1', '.vbs', '.js', '.xml']:
                    result = self.test_payload(campaign_id, payload, technique)
                    results.append(result)
        
        return results
    
    def test_payload(self, campaign_id, payload_path, technique):
        """Teste un payload individuel"""
        payload_name = payload_path.name
        print(f"   → Testing: {payload_name}")
        
        start_time = datetime.now()
        
        # Simuler l'exécution (en production, appeler le script PowerShell)
        # Pour l'exemple, on simule le résultat
        import random
        status = "bypass" if random.random() > 0.3 else "blocked"
        applocker_blocked = 0 if status == "bypass" else 1
        sysmon_events = random.randint(5, 50)
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        # Enregistrer le résultat
        result = {
            'campaign_id': campaign_id,
            'timestamp': start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'payload_name': payload_name,
            'technique': technique,
            'status': status,
            'applocker_blocked': applocker_blocked,
            'sysmon_events': sysmon_events,
            'execution_time': execution_time,
            'notes': f"Test automatique - {technique}"
        }
        
        self.save_result(result)
        
        status_icon = "✅" if status == "bypass" else "❌"
        print(f"      {status_icon} {status.upper()} | Sysmon: {sysmon_events} events | {execution_time:.2f}s")
        
        return result
    
    def save_result(self, result):
        """Enregistre un résultat dans la DB"""
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        
        c.execute("""
            INSERT INTO test_results 
            (campaign_id, timestamp, payload_name, technique, status, 
             applocker_blocked, sysmon_events, execution_time, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            result['campaign_id'],
            result['timestamp'],
            result['payload_name'],
            result['technique'],
            result['status'],
            result['applocker_blocked'],
            result['sysmon_events'],
            result['execution_time'],
            result['notes']
        ))
        
        conn.commit()
        conn.close()
    
    # ═══════════════════════════════════════════════════════
    # SCORING ET ANALYSE
    # ═══════════════════════════════════════════════════════
    
    def generate_scorecard(self, campaign_id):
        """Génère un tableau de scoring détaillé"""
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        
        # Score global
        c.execute("""
            SELECT technique, 
                   COUNT(*) as total,
                   SUM(CASE WHEN status='bypass' THEN 1 ELSE 0 END) as bypasses,
                   AVG(execution_time) as avg_time,
                   AVG(sysmon_events) as avg_events
            FROM test_results 
            WHERE campaign_id=?
            GROUP BY technique
        """, (campaign_id,))
        
        results = c.fetchall()
        conn.close()
        
        print("\n" + "="*70)
        print(f"📊 SCORECARD - Campagne {campaign_id}")
        print("="*70)
        print(f"{'Technique':<15} {'Total':<8} {'Bypass':<8} {'Taux':<10} {'Temps':<10} {'Events'}")
        print("-"*70)
        
        for row in results:
            technique, total, bypasses, avg_time, avg_events = row
            rate = (bypasses/total*100) if total > 0 else 0
            print(f"{technique:<15} {total:<8} {bypasses:<8} {rate:>6.1f}%    {avg_time:>6.2f}s    {avg_events:>6.1f}")
        
        print("="*70)
    
    def export_campaign_report(self, campaign_id, format="json"):
        """Exporte un rapport de campagne"""
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        
        # Récupérer toutes les données
        c.execute("SELECT * FROM campaigns WHERE id=?", (campaign_id,))
        campaign = c.fetchone()
        
        c.execute("SELECT * FROM test_results WHERE campaign_id=?", (campaign_id,))
        results = c.fetchall()
        
        conn.close()
        
        if format == "json":
            report = {
                'campaign': {
                    'id': campaign[0],
                    'name': campaign[1],
                    'description': campaign[2],
                    'start_time': campaign[3],
                    'end_time': campaign[4],
                    'status': campaign[5],
                    'total_tests': campaign[6],
                    'bypasses': campaign[7],
                    'blocked': campaign[8]
                },
                'results': [
                    {
                        'id': r[0],
                        'timestamp': r[2],
                        'payload': r[3],
                        'technique': r[4],
                        'status': r[5],
                        'applocker_blocked': r[6],
                        'sysmon_events': r[7],
                        'execution_time': r[8],
                        'notes': r[9]
                    }
                    for r in results
                ]
            }
            
            filename = self.campaigns_dir / f"campaign_{campaign_id}_report.json"
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            
            print(f"[+] Rapport JSON exporté: {filename}")
            return filename
    
    # ═══════════════════════════════════════════════════════
    # INTERFACE CLI
    # ═══════════════════════════════════════════════════════
    
    def list_campaigns(self):
        """Liste toutes les campagnes"""
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("SELECT * FROM campaigns ORDER BY id DESC")
        campaigns = c.fetchall()
        conn.close()
        
        print("\n📋 Campagnes de Tests")
        print("="*80)
        print(f"{'ID':<5} {'Nom':<25} {'Statut':<12} {'Tests':<8} {'Bypass':<8} {'Taux'}")
        print("-"*80)
        
        for camp in campaigns:
            cid, name, desc, start, end, status, total, bypasses, blocked = camp
            rate = f"{(bypasses/total*100 if total>0 else 0):.1f}%" if status == 'completed' else "N/A"
            print(f"{cid:<5} {name:<25} {status:<12} {total:<8} {bypasses:<8} {rate}")
        
        print("="*80)


# ═══════════════════════════════════════════════════════
# EXEMPLE D'UTILISATION
# ═══════════════════════════════════════════════════════

if __name__ == "__main__":
    import sys
    
    manager = CampaignManager()
    
    if len(sys.argv) < 2:
        print("""
Usage:
    python campaign_manager.py new <nom> [description]    - Créer une campagne
    python campaign_manager.py run <campaign_id>           - Lancer une campagne
    python campaign_manager.py end <campaign_id>           - Terminer une campagne
    python campaign_manager.py score <campaign_id>         - Afficher le scorecard
    python campaign_manager.py export <campaign_id>        - Exporter le rapport
    python campaign_manager.py list                        - Lister les campagnes
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "new":
        name = sys.argv[2] if len(sys.argv) > 2 else "Test Campaign"
        desc = sys.argv[3] if len(sys.argv) > 3 else ""
        campaign_id = manager.create_campaign(name, desc)
        print(f"\n✅ Campagne {campaign_id} créée. Lancez avec: python campaign_manager.py run {campaign_id}")
    
    elif command == "run":
        campaign_id = int(sys.argv[2])
        manager.run_campaign(campaign_id)
        print(f"\n✅ Campagne {campaign_id} terminée. Voir résultats: python campaign_manager.py score {campaign_id}")
    
    elif command == "end":
        campaign_id = int(sys.argv[2])
        stats = manager.end_campaign(campaign_id)
    
    elif command == "score":
        campaign_id = int(sys.argv[2])
        manager.generate_scorecard(campaign_id)
    
    elif command == "export":
        campaign_id = int(sys.argv[2])
        manager.export_campaign_report(campaign_id)
    
    elif command == "list":
        manager.list_campaigns()
    
    else:
        print(f"❌ Commande inconnue: {command}")