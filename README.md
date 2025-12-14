<div align="center">

# 🚀 Uranus Group - Plateforme Web Professionnelle

<div>
  <img src="https://img.shields.io/badge/Django-5.0.1-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Gemini_AI-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini AI"/>
</div>

### ✨ Plateforme complète pour QHSE & Informatique avec Chatbot IA

[![Security](https://img.shields.io/badge/Security-75%25-brightgreen?style=flat-square)](./PENTEST_REPORT.md)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=flat-square)](./PRODUCTION_READY.md)

---

</div>

## 📑 Table des Matières

- [🎯 Vue d'ensemble](#-vue-densemble)
- [✨ Fonctionnalités](#-fonctionnalités)
- [🛠️ Technologies](#️-technologies)
- [🚀 Installation](#-installation)
- [⚙️ Configuration](#️-configuration)
- [📱 Utilisation](#-utilisation)
- [🤖 Chatbot IA](#-chatbot-ia)
- [🔒 Sécurité](#-sécurité)
- [📊 Architecture](#-architecture)
- [🌐 Déploiement](#-déploiement)
- [🧪 Tests](#-tests)
- [📚 Documentation](#-documentation)
- [🤝 Contribution](#-contribution)
- [📞 Support](#-support)

---

## 🎯 Vue d'ensemble

**Uranus Group** est une plateforme web moderne et complète développée avec Django, spécialement conçue pour les entreprises spécialisées en **QHSE (Qualité, Hygiène, Sécurité, Environnement)** et **Informatique**.

### 🎨 Caractéristiques Principales

- 🎯 **Interface moderne** avec animations fluides (GSAP, AOS)
- 🤖 **Chatbot IA** intégré avec Google Gemini
- 📊 **Dashboard admin** complet avec graphiques
- 🔐 **Système de rôles** avancé (Admin, Manager QHSE, Manager Info, Client)
- 📱 **Design responsive** (mobile-first)
- 🚀 **Prêt pour la production** avec configuration optimisée
- 🔒 **Sécurité renforcée** (CSRF, XSS, SQL Injection protection)

---

## ✨ Fonctionnalités

### 🌐 Frontend Public

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0;">

<div style="background: linear-gradient(135deg, #0A1A2F 0%, #1a2f4f 100%); padding: 20px; border-radius: 10px; color: white;">

#### 🏠 Landing Page
- Slider animé avec images
- Sections QHSE/Informatique
- Certifications ISO
- Témoignages clients
- Animations GSAP

</div>

<div style="background: linear-gradient(135deg, #0DE1E7 0%, #0bc4c9 100%); padding: 20px; border-radius: 10px; color: #0A1A2F;">

#### 📋 Services
- Catalogue complet des services
- Filtrage par catégorie
- Pages détaillées
- Prix et durées

</div>

<div style="background: linear-gradient(135deg, #0A1A2F 0%, #1a2f4f 100%); padding: 20px; border-radius: 10px; color: white;">

#### 📰 Blog/CMS
- Articles avec catégories
- Système de commentaires
- Images mises en avant
- Recherche et filtres

</div>

<div style="background: linear-gradient(135deg, #0DE1E7 0%, #0bc4c9 100%); padding: 20px; border-radius: 10px; color: #0A1A2F;">

#### 📞 Contact
- Formulaire de contact
- Envoi d'email automatique
- Confirmation client
- Gestion des messages

</div>

</div>

### 👤 Espace Client

- ✅ **Tableau de bord personnalisé**
- ✅ **Création de demandes de service**
- ✅ **Suivi des demandes** (statut, historique)
- ✅ **Téléchargement de livrables**
- ✅ **Gestion du profil** (avatar, informations)
- ✅ **Historique complet**

### 🛡️ Espace Admin Personnalisé

<div style="background: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #0DE1E7; margin: 20px 0;">

#### 📊 Dashboard Principal
- Statistiques en temps réel
- Graphiques Chart.js interactifs
- Demandes récentes
- Actions rapides

#### 👥 Gestion Complète
- **Utilisateurs** : CRUD complet, rôles, permissions
- **Services** : Catégories, services, prix
- **Demandes** : Assignation, statuts, priorités
- **Articles** : Blog, catégories, publications
- **Contenu** : Certifications, témoignages, slider, équipe
- **Support** : Tickets, messages, résolutions

#### 📄 Fonctionnalités Avancées
- Export PDF des demandes
- Recherche et filtres avancés
- Notifications internes
- Gestion des tickets support

</div>

### 🤖 Chatbot IA Gemini

<div style="background: linear-gradient(135deg, #4285F4 0%, #34A853 100%); padding: 20px; border-radius: 10px; color: white; margin: 20px 0;">

- 💬 **Interface moderne** avec animations
- 🧠 **Réponses intelligentes** générées par Gemini
- 🎯 **Contexte personnalisé** pour Uranus Group
- ⚡ **Réponses rapides** avec gemini-2.5-flash
- 🔒 **Sécurisé** (CSRF, validation, protection XSS)
- 📱 **Responsive** et accessible

</div>

---

## 🛠️ Technologies

### Backend

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 20px 0;">

- **Django 5.0.1** - Framework web principal
- **Django REST Framework 3.16.1** - API REST
- **PostgreSQL** - Base de données (production)
- **SQLite** - Base de données (développement)
- **Redis** - Cache (production)
- **Gunicorn** - Serveur WSGI
- **WhiteNoise** - Fichiers statiques

</div>

### Frontend

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 20px 0;">

- **Tailwind CSS** - Framework CSS utilitaire
- **GSAP 3.12.5** - Animations avancées
- **AOS** - Animations au scroll
- **Chart.js** - Graphiques et statistiques
- **Font Awesome** - Icônes
- **JavaScript ES6+** - Code moderne

</div>

### IA & Outils

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 20px 0;">

- **Google Gemini AI** - Chatbot intelligent
- **ReportLab** - Génération PDF
- **Pillow** - Traitement d'images
- **python-decouple** - Variables d'environnement

</div>

---

## 🚀 Installation

### 📋 Prérequis

```bash
# Vérifier Python
python3 --version  # Doit être 3.11+

# Vérifier pip
pip3 --version
```

### 🔧 Installation Rapide

<div style="background: #0A1A2F; color: #0DE1E7; padding: 20px; border-radius: 10px; margin: 20px 0;">

```bash
# 1. Cloner ou naviguer vers le projet
cd /home/maxime/newC_uranusgroup_V

# 2. Créer l'environnement virtuel
python3 -m venv venv

# 3. Activer l'environnement virtuel
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# 6. Créer un superutilisateur
python manage.py createsuperuser

# 7. Collecter les fichiers statiques
python manage.py collectstatic --noinput

# 8. Lancer le serveur
python manage.py runserver
```

</div>

### 🎯 Accès

Une fois le serveur lancé, accédez à :

- 🌐 **Site web** : http://127.0.0.1:8000/
- 🔐 **Admin Django** : http://127.0.0.1:8000/admin/
- 🛡️ **Dashboard Admin** : http://127.0.0.1:8000/dashboard/admin/
- 📊 **Dashboard Client** : http://127.0.0.1:8000/dashboard/
- 🤖 **API REST** : http://127.0.0.1:8000/api/
- ❤️ **Health Check** : http://127.0.0.1:8000/health/

---

## ⚙️ Configuration

### 🔑 Variables d'Environnement

Créez un fichier `.env` à la racine du projet :

<div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0;">

```env
# Sécurité
SECRET_KEY=votre-clé-secrète-générée
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de données (Production)
DB_NAME=uranusgroup
DB_USER=postgres
DB_PASSWORD=votre-mot-de-passe
DB_HOST=localhost
DB_PORT=5432

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-de-passe-app
DEFAULT_FROM_EMAIL=noreply@uranusgroup.com

# Gemini AI
GEMINI_API_KEY=votre-clé-api-gemini

# Redis (Production)
REDIS_URL=redis://127.0.0.1:6379/1

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

</div>

### 🗄️ Configuration Base de Données

#### Développement (SQLite)
Par défaut, SQLite est utilisé en développement. Aucune configuration supplémentaire nécessaire.

#### Production (PostgreSQL)

```bash
# Installer PostgreSQL
sudo apt-get install postgresql postgresql-contrib

# Créer la base de données
sudo -u postgres psql
CREATE DATABASE uranusgroup;
CREATE USER uranususer WITH PASSWORD 'votre-mot-de-passe';
GRANT ALL PRIVILEGES ON DATABASE uranusgroup TO uranususer;
\q
```

---

## 📱 Utilisation

### 👤 Pour les Clients

1. **Créer un compte** : `/accounts/register/`
2. **Se connecter** : `/accounts/login/`
3. **Accéder au dashboard** : `/dashboard/`
4. **Créer une demande** : Depuis le dashboard
5. **Consulter les livrables** : Section "Mes livrables"

### 🛡️ Pour les Administrateurs

1. **Se connecter** avec un compte admin
2. **Accéder au dashboard admin** : `/dashboard/admin/`
3. **Gérer les utilisateurs** : Menu "Utilisateurs"
4. **Gérer les services** : Menu "Services"
5. **Suivre les demandes** : Menu "Demandes"
6. **Gérer le contenu** : Menus dédiés

### 🤖 Utiliser le Chatbot

1. Cliquez sur le **bouton flottant** en bas à droite
2. Posez votre question dans le chat
3. Recevez une réponse intelligente en temps réel
4. Le chatbot est disponible sur toutes les pages

---

## 🤖 Chatbot IA

### 🎯 Fonctionnalités

Le chatbot utilise **Google Gemini AI** pour fournir des réponses intelligentes sur :

- ✅ Services QHSE et Informatique
- ✅ Certifications ISO
- ✅ Processus et procédures
- ✅ Orientation vers les services appropriés

### 🔧 Configuration

La clé API Gemini est configurée dans `settings.py` :

```python
GEMINI_API_KEY = config('GEMINI_API_KEY', default='votre-clé')
```

### 📝 Personnalisation

Le prompt système peut être modifié dans `core/views.py` :

```python
system_prompt = """Tu es un assistant virtuel pour Uranus Group..."""
```

Voir [CHATBOT_README.md](./CHATBOT_README.md) pour plus de détails.

---

## 🔒 Sécurité

### 🛡️ Mesures Implémentées

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0;">

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">

**✅ CSRF Protection**
- Middleware activé
- Tokens sur tous les formulaires

</div>

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">

**✅ XSS Protection**
- Échappement automatique Django
- Validation des entrées

</div>

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">

**✅ SQL Injection**
- ORM Django
- Requêtes paramétrées

</div>

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">

**✅ Headers Sécurité**
- X-Frame-Options: DENY
- X-Content-Type-Nosniff
- X-XSS-Protection

</div>

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">

**✅ Authentification**
- Hashage des mots de passe
- Sessions sécurisées
- Cookies HttpOnly

</div>

<div style="background: #d4edda; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">

**✅ Autorisation**
- Système de rôles
- Permissions granulaires
- Protection des routes

</div>

</div>

### 🧪 Tests de Sécurité

Exécutez les tests de pénétration :

```bash
# Tous les tests
./run_full_pentest.sh

# Tests individuels
python security_audit.py
python security_tests.py
python chatbot_security_tests.py
```

**Score de sécurité : 75%** ✅

Voir [PENTEST_REPORT.md](./PENTEST_REPORT.md) pour le rapport complet.

---

## 📊 Architecture

### 📁 Structure du Projet

```
uranusgroup/
├── 📂 accounts/          # Gestion utilisateurs
│   ├── models.py         # User, UserProfile
│   ├── views.py          # Authentification
│   └── urls.py
│
├── 📂 blog/              # Blog/CMS
│   ├── models.py         # Article, Category
│   ├── views.py
│   └── urls.py
│
├── 📂 core/              # Pages principales
│   ├── models.py         # ContactMessage, TeamMember, SliderItem
│   ├── views.py          # Home, contact, about, chatbot
│   └── urls.py
│
├── 📂 dashboard/         # Dashboard admin
│   ├── models.py         # Notification, SupportTicket
│   ├── views.py          # Vues admin
│   └── urls.py
│
├── 📂 services/          # Services QHSE/Info
│   ├── models.py         # Service, ServiceRequest, Deliverable
│   ├── api.py            # API REST
│   ├── serializers.py
│   └── urls.py
│
├── 📂 health_check/      # Monitoring
│   └── views.py
│
├── 📂 templates/         # Templates HTML
│   ├── base.html
│   ├── accounts/
│   ├── blog/
│   ├── core/
│   ├── dashboard/
│   └── services/
│
├── 📂 static/           # Fichiers statiques
│   ├── css/
│   ├── js/
│   └── images/
│
├── 📂 media/            # Fichiers uploadés
│
├── 📂 uranusgroup/      # Configuration
│   ├── settings.py      # Settings développement
│   ├── settings_production.py  # Settings production
│   └── urls.py
│
└── 📄 manage.py
```

### 🔄 Flux de Données

```
Client → URL → View → Model → Database
                ↓
            Template → Response
```

### 🎨 Design System

<div style="background: linear-gradient(135deg, #0A1A2F 0%, #1a2f4f 100%); padding: 20px; border-radius: 10px; color: white; margin: 20px 0;">

**Couleurs Principales**
- 🔵 Primaire foncé : `#0A1A2F`
- 🔷 Primaire cyan : `#0DE1E7`
- ⚪ Blanc : `#FFFFFF`

**Typographie**
- Police : Inter, système de polices modernes
- Taille : Responsive (mobile-first)

**Animations**
- GSAP pour les animations complexes
- AOS pour les animations au scroll
- Transitions CSS fluides

</div>

---

## 🌐 Déploiement

### 🚀 Production

<div style="background: #fff3cd; padding: 20px; border-radius: 10px; border-left: 4px solid #ffc107; margin: 20px 0;">

#### 📋 Checklist Pré-Déploiement

- [ ] Générer une nouvelle SECRET_KEY
- [ ] Configurer DEBUG = False
- [ ] Configurer ALLOWED_HOSTS
- [ ] Configurer PostgreSQL
- [ ] Configurer Redis
- [ ] Configurer SMTP pour emails
- [ ] Configurer la clé API Gemini
- [ ] Collecter les fichiers statiques
- [ ] Configurer Nginx
- [ ] Configurer Gunicorn
- [ ] Obtenir un certificat SSL

</div>

### 📝 Guide Complet

Consultez [DEPLOYMENT.md](./DEPLOYMENT.md) pour le guide complet de déploiement.

### 🔧 Scripts de Déploiement

```bash
# Déploiement automatique
./deploy.sh

# Sauvegarde
./backup.sh

# Gestion production
python manage_production.py [command]
```

---

## 🧪 Tests

### 🔍 Tests de Sécurité

```bash
# Audit de configuration
python security_audit.py

# Tests de pénétration
python security_tests.py

# Tests chatbot
python chatbot_security_tests.py

# Tous les tests
./run_full_pentest.sh
```

### ✅ Tests Django

```bash
# Tous les tests
python manage.py test

# Tests d'une app spécifique
python manage.py test accounts
python manage.py test services
```

---

## 📚 Documentation

### 📄 Documents Disponibles

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">

- [📊 ANALYSE_PROJET.md](./ANALYSE_PROJET.md) - Analyse complète du projet
- [🔒 PENTEST_REPORT.md](./PENTEST_REPORT.md) - Rapport de pénétration
- [🚀 DEPLOYMENT.md](./DEPLOYMENT.md) - Guide de déploiement
- [✅ PRODUCTION_CHECKLIST.md](./PRODUCTION_CHECKLIST.md) - Checklist production
- [🤖 CHATBOT_README.md](./CHATBOT_README.md) - Documentation chatbot
- [🛡️ ADMIN_FEATURES.md](./ADMIN_FEATURES.md) - Fonctionnalités admin
- [🔐 SECURITY_SUMMARY.md](./SECURITY_SUMMARY.md) - Résumé sécurité

</div>

---

## 🤝 Contribution

### 📝 Guidelines

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### 🔍 Code Review

- Respecter les conventions PEP 8
- Ajouter des tests pour les nouvelles fonctionnalités
- Documenter le code
- Vérifier la sécurité

---

## 📞 Support

### 💬 Contact

- 📧 Email : contact@uranusgroup.com
- 🌐 Site web : https://uranusgroup.com
- 📱 Téléphone : +33 1 XX XX XX XX

### 🐛 Signaler un Bug

Ouvrez une issue sur le dépôt avec :
- Description du bug
- Steps to reproduce
- Comportement attendu
- Screenshots (si applicable)

### 💡 Suggestions

Les suggestions sont les bienvenues ! Ouvrez une issue avec le tag `enhancement`.

---

## 📄 Licence

**Propriétaire - Uranus Group © 2024**

Tous droits réservés. Ce projet est la propriété exclusive d'Uranus Group.

---

## 🎉 Remerciements

- Django Community
- Tailwind CSS
- Google Gemini AI
- Tous les contributeurs

---

<div align="center">

### ⭐ Si ce projet vous a aidé, n'hésitez pas à lui donner une étoile !

**Fait avec ❤️ par l'équipe Uranus Group**

[⬆ Retour en haut](#-uranus-group---plateforme-web-professionnelle)

</div>

---

<div align="center" style="margin-top: 50px; padding: 20px; background: linear-gradient(135deg, #0A1A2F 0%, #1a2f4f 100%); border-radius: 10px; color: #0DE1E7;">

**🚀 Prêt à démarrer ? Suivez le guide d'installation ci-dessus !**

</div>
