#!/bin/bash
# Script de déploiement pour la production

set -e  # Arrêter en cas d'erreur

echo "🚀 Déploiement Uranus Group en production..."

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements_production.txt

# Collecter les fichiers statiques
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

# Appliquer les migrations
echo "🗄️  Application des migrations..."
python manage.py migrate --noinput

# Créer les répertoires nécessaires
mkdir -p logs
mkdir -p media
mkdir -p staticfiles

# Vérifier la configuration
echo "✅ Vérification de la configuration..."
python manage.py check --deploy

# Redémarrer Gunicorn (si déjà en cours)
if systemctl is-active --quiet gunicorn-uranusgroup; then
    echo "🔄 Redémarrage de Gunicorn..."
    sudo systemctl restart gunicorn-uranusgroup
else
    echo "⚠️  Gunicorn n'est pas en cours d'exécution. Démarrez-le avec:"
    echo "   sudo systemctl start gunicorn-uranusgroup"
fi

# Redémarrer Nginx (si configuré)
if systemctl is-active --quiet nginx; then
    echo "🔄 Redémarrage de Nginx..."
    sudo systemctl reload nginx
fi

echo "✅ Déploiement terminé avec succès!"

