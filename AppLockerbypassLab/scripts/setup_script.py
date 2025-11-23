#!/usr/bin/env python3
"""
Setup Script - Installation et Configuration Automatique
AppLocker Bypass Lab Framework
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class LabSetup:
    """Gestionnaire d'installation du lab"""
    
    def __init__(self):
        self.base_dir = Path.cwd()
        self.required_dirs = [
            "payloads", "payloads/mshta", "payloads/regsvr32",
            "payloads/rundll32", "payloads/installutil", "payloads/msbuild",
            "payloads/bat", "payloads/ps1", "payloads/vbs", "payloads/xml",
            "payloads/obfuscated", "payloads/packaged", "payloads/generated",
            "scripts", "logs", "logs/sysmon", "logs/applocker",
            "campaigns", "lab_vm"
        ]
        
    def print_banner(self):
        """Affiche le banner"""
        banner = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║          🛡️  AppLocker Bypass Lab - Setup Script 🛡️            ║
║                                                                  ║
║  Framework d'Automatisation pour Tests LOLBAS/MITRE             ║
║  Usage Éducatif et Défensif Uniquement                          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
        print(banner)
    
    def check_system(self):
        """Vérifie le système d'exploitation"""
        print("\n[*] Vérification du système...")
        
        if platform.system() != "Windows":
            print("    ⚠️  Ce framework est conçu pour Windows 10/11")
            print("    Vous pouvez continuer, mais certaines fonctionnalités seront limitées")
            return False
        
        print("    ✅ Windows détecté")
        
        # Vérifier Python version
        py_version = sys.version_info
        if py_version.major < 3 or (py_version.major == 3 and py_version.minor < 8):
            print(f"    ❌ Python 3.8+ requis (vous avez {py_version.major}.{py_version.minor})")
            return False
        
        print(f"    ✅ Python {py_version.major}.{py_version.minor}.{py_version.micro}")
        
        return True
    
    def create_directories(self):
        """Crée l'arborescence du lab"""
        print("\n[*] Création de l'arborescence...")
        
        for dir_path in self.required_dirs:
            full_path = self.base_dir / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"    ✅ {dir_path}")
    
    def install_dependencies(self):
        """Installe les dépendances Python"""
        print("\n[*] Installation des dépendances Python...")
        
        dependencies = [
            "flask",
            "requests"
        ]
        
        for dep in dependencies:
            try:
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", dep, "-q"
                ])
                print(f"    ✅ {dep}")
            except subprocess.CalledProcessError:
                print(f"    ❌ Erreur installation {dep}")
    
    def create_config_files(self):
        """Crée les fichiers de configuration"""
        print("\n[*] Création des fichiers de configuration...")
        
        # requirements.txt
        requirements = """flask>=2.0.0
requests>=2.25.0
"""
        with open(self.base_dir / "requirements.txt", "w") as f:
            f.write(requirements)
        print("    ✅ requirements.txt")
        
        # .gitignore
        gitignore = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# Lab specific
logs/
*.evtx
*.db
campaigns/
payloads/generated/
payloads/obfuscated/
payloads/packaged/

# VM files
lab_vm/*.vmx
lab_vm/*.vmdk
lab_vm/*.vmem

# IDE
.vscode/
.idea/
*.swp
"""
        with open(self.base_dir / ".gitignore", "w") as f:
            f.write(gitignore)
        print("    ✅ .gitignore")
        
        # config.json
        config = """{
  "lab": {
    "name": "AppLockerBypassLab",
    "version": "1.0.0",
    "vm_path": "lab_vm/snapshot.vmx"
  },
  "sysmon": {
    "config": "https://raw.githubusercontent.com/SwiftOnSecurity/sysmon-config/master/sysmonconfig-export.xml",
    "enabled": true
  },
  "applocker": {
    "mode": "audit",
    "rules": []
  },
  "dashboard": {
    "host": "0.0.0.0",
    "port": 5000,
    "debug": true
  }
}
"""
        with open(self.base_dir / "config.json", "w") as f:
            f.write(config)
        print("    ✅ config.json")
    
    def check_powershell(self):
        """Vérifie PowerShell"""
        print("\n[*] Vérification PowerShell...")
        
        try:
            result = subprocess.run(
                ["powershell", "-Command", "$PSVersionTable.PSVersion.Major"],
                capture_output=True,
                text=True
            )
            version = result.stdout.strip()
            
            if int(version) >= 5:
                print(f"    ✅ PowerShell {version}.x détecté")
                return True
            else:
                print(f"    ⚠️  PowerShell {version}.x (5.1+ recommandé)")
                return False
        except:
            print("    ❌ PowerShell non trouvé")
            return False
    
    def check_admin_rights(self):
        """Vérifie les droits administrateur"""
        print("\n[*] Vérification des privilèges...")
        
        if platform.system() == "Windows":
            try:
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin()
                
                if is_admin:
                    print("    ✅ Droits administrateur détectés")
                    return True
                else:
                    print("    ⚠️  Pas de droits administrateur")
                    print("        Certaines fonctionnalités nécessitent des privilèges élevés")
                    return False
            except:
                print("    ⚠️  Impossible de vérifier les privilèges")
                return False
        
        return True
    
    def create_quick_start_script(self):
        """Crée un script de démarrage rapide"""
        print("\n[*] Création du script de démarrage rapide...")
        
        # Script Batch Windows
        batch_script = """@echo off
echo ============================================
echo AppLocker Bypass Lab - Quick Start
echo ============================================
echo.

echo [1] Telecharger les payloads
python scripts\\download_payloads.py
echo.

echo [2] Generer les payloads personnalises
python scripts\\generate_payloads.py
echo.

echo [3] Lancer le dashboard
start python scripts\\dashboard.py
echo Dashboard demarre sur http://localhost:5000
echo.

echo [4] Creer une campagne de test
python scripts\\campaign_manager.py new "Test Initial" "Premiere campagne"
echo.

echo ============================================
echo Setup termine! Consultez le README.md
echo ============================================
pause
"""
        with open(self.base_dir / "quickstart.bat", "w") as f:
            f.write(batch_script)
        print("    ✅ quickstart.bat")
        
        # Script Shell Linux/Mac
        shell_script = """#!/bin/bash
echo "============================================"
echo "AppLocker Bypass Lab - Quick Start"
echo "============================================"
echo ""

echo "[1] Télécharger les payloads"
python3 scripts/download_payloads.py
echo ""

echo "[2] Générer les payloads personnalisés"
python3 scripts/generate_payloads.py
echo ""

echo "[3] Lancer le dashboard"
python3 scripts/dashboard.py &
echo "Dashboard démarré sur http://localhost:5000"
echo ""

echo "============================================"
echo "Setup terminé! Consultez le README.md"
echo "============================================"
"""
        with open(self.base_dir / "quickstart.sh", "w") as f:
            f.write(shell_script)
        
        # Rendre exécutable sur Unix
        if platform.system() != "Windows":
            os.chmod(self.base_dir / "quickstart.sh", 0o755)
        
        print("    ✅ quickstart.sh")
    
    def print_post_install_instructions(self):
        """Affiche les instructions post-installation"""
        print("\n" + "="*70)
        print("✅ INSTALLATION TERMINÉE")
        print("="*70)
        
        print("\n📋 PROCHAINES ÉTAPES:\n")
        
        print("1️⃣  Configuration de la VM de test")
        print("   • Créer une VM Windows 10/11")
        print("   • Installer Sysmon avec sysmonconfig.xml")
        print("   • Configurer AppLocker en mode Audit")
        print("   • Créer un snapshot initial")
        
        print("\n2️⃣  Téléchargement des payloads")
        print("   python scripts/download_payloads.py")
        
        print("\n3️⃣  Génération des payloads personnalisés")
        print("   python scripts/generate_payloads.py")
        
        print("\n4️⃣  Obfuscation des payloads")
        print("   python scripts/obfuscate_payloads.py")
        
        print("\n5️⃣  Packaging des payloads")
        print("   python scripts/package_payloads.py")
        
        print("\n6️⃣  Lancement du dashboard")
        print("   python scripts/dashboard.py")
        print("   → http://localhost:5000")
        
        print("\n7️⃣  Création d'une campagne")
        print("   python scripts/campaign_manager.py new \"Première Campagne\"")
        
        print("\n8️⃣  Exécution des tests")
        print("   powershell .\\scripts\\execute_payloads.ps1")
        
        print("\n" + "="*70)
        print("📚 DOCUMENTATION COMPLÈTE: README.md")
        print("⚠️  RAPPEL: Usage éducatif et défensif uniquement")
        print("="*70 + "\n")
    
    def run(self):
        """Exécute l'installation complète"""
        self.print_banner()
        
        # Vérifications
        if not self.check_system():
            print("\n⚠️  Avertissement: système non optimal détecté")
            response = input("Continuer quand même? (y/N): ")
            if response.lower() != 'y':
                print("Installation annulée.")
                sys.exit(1)
        
        self.check_powershell()
        self.check_admin_rights()
        
        # Installation
        self.create_directories()
        self.install_dependencies()
        self.create_config_files()
        self.create_quick_start_script()
        
        # Instructions finales
        self.print_post_install_instructions()


# ═══════════════════════════════════════════════════════
# POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        installer = LabSetup()
        installer.run()
    except KeyboardInterrupt:
        print("\n\n❌ Installation annulée par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur lors de l'installation: {e}")
        sys.exit(1)
