# Uranus Group - Site Web Professionnel

Site web complet et moderne pour Uranus Group, spécialisé en QHSE (Qualité, Hygiène, Sécurité, Environnement) et Informatique.

## 🚀 Fonctionnalités

### Frontend
- **Landing page animée** avec slider, sections QHSE/Informatique, certifications, témoignages
- **Pages détaillées** pour chaque service
- **Blog/CMS interne** pour gérer articles et catégories
- **Page À propos** avec présentation de l'équipe
- **Page Contact** avec formulaire et envoi d'email automatique
- **Design responsive** avec Tailwind CSS
- **Animations** avec GSAP et AOS

### Backend
- **Espace utilisateur sécurisé** :
  - Tableau de bord personnalisé
  - Création de demandes de service
  - Historique des demandes
  - Téléchargement de livrables
  - Gestion du profil

- **Espace admin personnalisé** (pas l'admin Django standard) :
  - Dashboard avec statistiques et graphiques Chart.js
  - Gestion des utilisateurs
  - Gestion des services
  - Gestion des demandes
  - Gestion des articles
  - Gestion des tickets support

- **Système de rôles** :
  - Administrateur
  - Manager QHSE
  - Manager Informatique
  - Client

- **Sécurité** :
  - CSRF protection
  - Validation des données
  - Hashage des mots de passe
  - Protection des routes selon les rôles

- **Fonctionnalités avancées** :
  - Système de notifications internes
  - Système de tickets support
  - Export PDF des demandes
  - API REST pour application mobile future

## 🛠️ Technologies

- **Backend** : Django 5.0.1
- **Base de données** : SQLite
- **Frontend** : Tailwind CSS, JavaScript moderne
- **Animations** : GSAP, AOS
- **Graphiques** : Chart.js
- **API** : Django REST Framework
- **PDF** : ReportLab

## 📦 Installation

### Prérequis
- Python 3.11+
- pip
- virtualenv (recommandé)

### Étapes

1. **Cloner le projet** (ou naviguer vers le répertoire)
```bash
cd /home/maxime/newC_uranusgroup_V
```

2. **Créer et activer l'environnement virtuel**
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Linux/Mac
# ou
venv\Scripts\activate  # Sur Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Appliquer les migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

6. **Collecter les fichiers statiques** (optionnel en développement)
```bash
python manage.py collectstatic --noinput
```

7. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

Le site sera accessible à l'adresse : http://127.0.0.1:8000/

## 📁 Structure du projet

```
uranusgroup/
├── accounts/          # Gestion des utilisateurs et authentification
├── blog/              # Blog/CMS interne
├── core/              # Pages principales (home, contact, about)
├── dashboard/         # Dashboard admin personnalisé
├── services/          # Services QHSE et Informatique
├── templates/         # Templates HTML
├── static/            # Fichiers statiques (CSS, JS, images)
├── media/             # Fichiers uploadés (images, documents)
├── uranusgroup/       # Configuration du projet
└── manage.py
```

## 🎨 Design

- **Couleurs principales** :
  - Primaire foncé : `#0A1A2F`
  - Primaire cyan : `#0DE1E7`
  - Blanc : `#FFFFFF`

- **Typographie** : Inter, système de polices modernes

## 🔐 Sécurité

- Protection CSRF activée
- Validation des données côté serveur
- Hashage des mots de passe (Django par défaut)
- Protection des routes selon les rôles
- Authentification requise pour les zones sensibles

## 📧 Configuration Email

Pour activer l'envoi d'emails réels, modifiez les paramètres dans `uranusgroup/settings.py` :

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre-email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe'
DEFAULT_FROM_EMAIL = 'noreply@uranusgroup.com'
```

## 🔌 API REST

L'API REST est disponible à l'adresse `/api/` pour une future application mobile.

Endpoints disponibles :
- `/api/services/` - Liste des services
- `/api/categories/` - Catégories de services
- `/api/requests/` - Demandes de service
- `/api/deliverables/` - Livrables

Authentification requise pour la plupart des endpoints.

## 📄 Export PDF

Les demandes de service peuvent être exportées en PDF via le dashboard admin.

## 👥 Rôles et permissions

- **Administrateur** : Accès complet à toutes les fonctionnalités
- **Manager QHSE** : Gestion des services et demandes QHSE
- **Manager Informatique** : Gestion des services et demandes Informatique
- **Client** : Création de demandes, consultation de ses livrables

## 🚀 Déploiement

Pour la production :
1. Modifiez `DEBUG = False` dans `settings.py`
2. Configurez `ALLOWED_HOSTS`
3. Utilisez une base de données PostgreSQL ou MySQL
4. Configurez les fichiers statiques avec un serveur web (Nginx, Apache)
5. Utilisez Gunicorn ou uWSGI pour servir l'application

## 📝 Notes

- Le projet utilise SQLite par défaut (idéal pour le développement)
- Les fichiers média sont stockés dans le dossier `media/`
- Les fichiers statiques sont dans `static/`
- L'admin Django standard est toujours accessible à `/admin/` pour la gestion de base

## 🤝 Contribution

Ce projet a été créé pour Uranus Group. Pour toute modification, contactez l'équipe de développement.

## 📄 Licence

Propriétaire - Uranus Group © 2024
