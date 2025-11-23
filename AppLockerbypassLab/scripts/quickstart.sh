#!/bin/bash
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
