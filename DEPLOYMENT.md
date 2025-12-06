# Guide de Déploiement en Production - Uranus Group

## 📋 Checklist de Production

### ✅ Sécurité
- [x] `DEBUG = False`
- [x] `SECRET_KEY` sécurisé (variable d'environnement)
- [x] `ALLOWED_HOSTS` configuré
- [x] HTTPS activé
- [x] Headers de sécurité configurés
- [x] CSRF et cookies sécurisés
- [x] HSTS activé

### ✅ Base de données
- [x] PostgreSQL configuré
- [x] Migrations appliquées
- [x] Backup automatique configuré

### ✅ Fichiers statiques et média
- [x] `collectstatic` configuré
- [x] WhiteNoise ou serveur web pour les statiques
- [x] Stockage média configuré

### ✅ Performance
- [x] Cache Redis configuré
- [x] Compression activée
- [x] Gunicorn configuré

### ✅ Monitoring
- [x] Logging configuré
- [x] Emails d'erreur configurés
- [x] Health check disponible

## 🚀 Étapes de Déploiement

### 1. Préparation du Serveur

```bash
# Mettre à jour le système
sudo apt update && sudo apt upgrade -y

# Installer les dépendances
sudo apt install -y python3-pip python3-venv postgresql postgresql-contrib nginx redis-server certbot python3-certbot-nginx

# Créer un utilisateur pour l'application
sudo adduser --disabled-password --gecos "" uranusgroup
```

### 2. Configuration PostgreSQL

```bash
# Se connecter à PostgreSQL
sudo -u postgres psql

# Créer la base de données et l'utilisateur
CREATE DATABASE uranusgroup;
CREATE USER uranusgroup_user WITH PASSWORD 'votre-mot-de-passe-securise';
ALTER ROLE uranusgroup_user SET client_encoding TO 'utf8';
ALTER ROLE uranusgroup_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE uranusgroup_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE uranusgroup TO uranusgroup_user;
\q
```

### 3. Déploiement de l'Application

```bash
# Cloner ou copier le projet
cd /var/www
sudo git clone votre-repo uranusgroup
sudo chown -R uranusgroup:uranusgroup uranusgroup
cd uranusgroup

# Créer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements_production.txt

# Copier et configurer .env
cp .env.example .env
nano .env  # Éditer avec vos valeurs

# Générer un SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Copier la clé dans .env
```

### 4. Configuration Django

```bash
# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Créer les répertoires
mkdir -p logs media staticfiles
chmod -R 755 media staticfiles
```

### 5. Configuration Gunicorn

```bash
# Copier le fichier de service
sudo cp systemd_gunicorn.service.example /etc/systemd/system/gunicorn-uranusgroup.service

# Éditer le fichier avec vos chemins
sudo nano /etc/systemd/system/gunicorn-uranusgroup.service

# Activer et démarrer le service
sudo systemctl daemon-reload
sudo systemctl enable gunicorn-uranusgroup
sudo systemctl start gunicorn-uranusgroup
sudo systemctl status gunicorn-uranusgroup
```

### 6. Configuration Nginx

```bash
# Copier la configuration
sudo cp nginx.conf.example /etc/nginx/sites-available/uranusgroup

# Éditer avec votre domaine
sudo nano /etc/nginx/sites-available/uranusgroup

# Activer le site
sudo ln -s /etc/nginx/sites-available/uranusgroup /etc/nginx/sites-enabled/

# Tester la configuration
sudo nginx -t

# Redémarrer Nginx
sudo systemctl restart nginx
```

### 7. Configuration SSL (Let's Encrypt)

```bash
# Obtenir un certificat SSL
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Renouvellement automatique (déjà configuré par certbot)
sudo certbot renew --dry-run
```

### 8. Configuration Redis

```bash
# Redis devrait déjà être démarré
sudo systemctl status redis

# Vérifier la connexion
redis-cli ping
```

### 9. Configuration des Backups

```bash
# Rendre le script exécutable
chmod +x backup.sh

# Ajouter au crontab (sauvegarde quotidienne à 2h du matin)
crontab -e
# Ajouter: 0 2 * * * /path/to/your/project/backup.sh
```

### 10. Monitoring

```bash
# Vérifier les logs
tail -f logs/django.log
tail -f logs/gunicorn_error.log

# Vérifier les services
sudo systemctl status gunicorn-uranusgroup
sudo systemctl status nginx
sudo systemctl status postgresql
sudo systemctl status redis
```

## 🔧 Commandes Utiles

### Redémarrer l'application
```bash
sudo systemctl restart gunicorn-uranusgroup
```

### Voir les logs
```bash
# Logs Django
tail -f logs/django.log

# Logs Gunicorn
tail -f logs/gunicorn_error.log
sudo journalctl -u gunicorn-uranusgroup -f

# Logs Nginx
sudo tail -f /var/log/nginx/error.log
```

### Mettre à jour l'application
```bash
cd /var/www/uranusgroup
source venv/bin/activate
git pull
pip install -r requirements_production.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn-uranusgroup
```

### Sauvegarder la base de données
```bash
./backup.sh
```

## 🔐 Sécurité Additionnelle

### Firewall (UFW)
```bash
sudo ufw allow 22/tcp  # SSH
sudo ufw allow 80/tcp  # HTTP
sudo ufw allow 443/tcp # HTTPS
sudo ufw enable
```

### Fail2Ban (protection contre les attaques)
```bash
sudo apt install fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

## 📊 Monitoring Recommandé

### Optionnel: Sentry pour le monitoring d'erreurs
```bash
pip install sentry-sdk
```

Puis dans `settings_production.py`:
```python
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.1,
    send_default_pii=False,
)
```

## ✅ Vérifications Post-Déploiement

1. ✅ Site accessible via HTTPS
2. ✅ Redirection HTTP → HTTPS fonctionne
3. ✅ Fichiers statiques servis correctement
4. ✅ Fichiers média accessibles
5. ✅ Base de données fonctionnelle
6. ✅ Cache Redis opérationnel
7. ✅ Emails envoyés correctement
8. ✅ Logs générés
9. ✅ Backups automatiques fonctionnels
10. ✅ Monitoring en place

## 🆘 Dépannage

### Erreur 502 Bad Gateway
- Vérifier que Gunicorn est démarré: `sudo systemctl status gunicorn-uranusgroup`
- Vérifier les logs: `sudo journalctl -u gunicorn-uranusgroup -n 50`

### Erreur 500
- Vérifier les logs Django: `tail -f logs/django_errors.log`
- Vérifier les permissions des fichiers
- Vérifier la configuration de la base de données

### Fichiers statiques non chargés
- Vérifier `collectstatic`: `python manage.py collectstatic --noinput`
- Vérifier les permissions: `chmod -R 755 staticfiles`
- Vérifier la configuration Nginx

## 📝 Notes Importantes

- Changez tous les mots de passe par défaut
- Gardez les dépendances à jour
- Surveillez les logs régulièrement
- Testez les backups régulièrement
- Mettez à jour le système régulièrement

