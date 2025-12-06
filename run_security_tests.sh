#!/bin/bash
# Script pour exécuter les tests de sécurité

echo "🔒 Tests de sécurité - Uranus Group"
echo "===================================="
echo ""

# Activer l'environnement virtuel
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Exécuter l'audit de sécurité
echo "1️⃣  Exécution de l'audit de sécurité..."
echo ""
python security_audit.py

echo ""
echo "2️⃣  Exécution des tests de pénétration..."
echo ""
python security_tests.py

echo ""
echo "✅ Tests terminés !"
echo ""
echo "Consultez les rapports ci-dessus pour les détails."

