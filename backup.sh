#!/bin/bash
# Script de sauvegarde de la base de données

set -e

BACKUP_DIR="/var/backups/uranusgroup"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/backup_$DATE.sql"

# Créer le répertoire de backup s'il n'existe pas
mkdir -p $BACKUP_DIR

# Charger les variables d'environnement
source .env

# Sauvegarder la base de données PostgreSQL
echo "💾 Sauvegarde de la base de données..."
PGPASSWORD=$DB_PASSWORD pg_dump -h $DB_HOST -U $DB_USER -d $DB_NAME > $BACKUP_FILE

# Compresser la sauvegarde
gzip $BACKUP_FILE

# Supprimer les sauvegardes de plus de 30 jours
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +30 -delete

# Sauvegarder les fichiers média (optionnel)
if [ -d "media" ]; then
    echo "📁 Sauvegarde des fichiers média..."
    tar -czf "$BACKUP_DIR/media_$DATE.tar.gz" media/
    find $BACKUP_DIR -name "media_*.tar.gz" -mtime +30 -delete
fi

echo "✅ Sauvegarde terminée: $BACKUP_FILE.gz"

