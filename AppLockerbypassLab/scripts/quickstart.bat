@echo off
echo ============================================
echo AppLocker Bypass Lab - Quick Start
echo ============================================
echo.

echo [1] Telecharger les payloads
python scripts\download_payloads.py
echo.

echo [2] Generer les payloads personnalises
python scripts\generate_payloads.py
echo.

echo [3] Lancer le dashboard
start python scripts\dashboard.py
echo Dashboard demarre sur http://localhost:5000
echo.

echo [4] Creer une campagne de test
python scripts\campaign_manager.py new "Test Initial" "Premiere campagne"
echo.

echo ============================================
echo Setup termine! Consultez le README.md
echo ============================================
pause
