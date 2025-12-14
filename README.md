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

---

## 🎯 Vue d'ensemble

**Uranus Group** est une plateforme web moderne et complète développée avec Django, spécialement conçue pour les entreprises spécialisées en **QHSE (Qualité, Hygiène, Sécurité, Environnement)** et **Informatique**.

### 📊 Schéma Global du Système

```mermaid
graph TB
    A[👤 Utilisateur] --> B{Type d'Utilisateur}
    B -->|Client| C[📱 Dashboard Client]
    B -->|Manager| D[🛡️ Dashboard Manager]
    B -->|Admin| E[⚙️ Dashboard Admin]
    
    C --> F[📝 Créer Demande]
    C --> G[📥 Télécharger Livrables]
    C --> H[👤 Gérer Profil]
    
    D --> I[📊 Gérer Demandes]
    D --> J[📤 Upload Livrables]
    D --> K[📈 Statistiques]
    
    E --> L[👥 Gestion Utilisateurs]
    E --> M[💼 Gestion Services]
    E --> N[📰 Gestion Blog]
    E --> O[🎫 Tickets Support]
    
    P[🤖 Chatbot IA] --> Q[💬 Gemini AI]
    Q --> R[📝 Réponses Intelligentes]
    
    style A fill:#0DE1E7
    style P fill:#4285F4
    style E fill:#0A1A2F,color:#fff
```

### 🎨 Caractéristiques Principales

<div align="center">

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  🎯 INTERFACE MODERNE                                       │
│  ├─ Animations GSAP & AOS                                  │
│  ├─ Design Responsive                                      │
│  └─ UX Optimisée                                            │
│                                                             │
│  🤖 CHATBOT IA                                              │
│  ├─ Google Gemini Integration                               │
│  ├─ Réponses Intelligentes                                 │
│  └─ Disponible 24/7                                        │
│                                                             │
│  📊 DASHBOARD COMPLET                                       │
│  ├─ Statistiques Temps Réel                                │
│  ├─ Graphiques Interactifs                                 │
│  └─ Gestion Centralisée                                     │
│                                                             │
│  🔐 SÉCURITÉ RENFORCÉE                                      │
│  ├─ CSRF Protection                                        │
│  ├─ XSS Protection                                          │
│  └─ SQL Injection Protection                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

</div>

---

## ✨ Fonctionnalités

### 🌐 Frontend Public

<details>
<summary><b>📊 Schéma Frontend - Cliquez pour voir</b></summary>

```mermaid
graph LR
    A[🏠 Landing Page] --> B[📋 Services]
    A --> C[📰 Blog]
    A --> D[👥 À Propos]
    A --> E[📞 Contact]
    
    B --> F[🔍 Recherche]
    B --> G[🏷️ Filtres]
    B --> H[📄 Détails]
    
    C --> I[📝 Articles]
    C --> J[🏷️ Catégories]
    C --> K[💬 Commentaires]
    
    E --> L[📧 Formulaire]
    E --> M[✉️ Email Auto]
    
    style A fill:#0DE1E7
    style B fill:#0A1A2F,color:#fff
    style C fill:#0DE1E7
```

</details>

#### 🏠 Landing Page

```
┌─────────────────────────────────────────────────┐
│  🎠 SLIDER ANIMÉ                                 │
│  ├─ Images dynamiques                           │
│  ├─ Transitions fluides                         │
│  └─ Call-to-action                              │
│                                                  │
│  📦 SECTIONS QHSE/INFO                          │
│  ├─ Services mis en avant                       │
│  ├─ Descriptions détaillées                    │
│  └─ Liens vers pages dédiées                    │
│                                                  │
│  🏆 CERTIFICATIONS                              │
│  ├─ Logos ISO                                   │
│  ├─ Badges qualité                              │
│  └─ Descriptions                                 │
│                                                  │
│  💬 TÉMOIGNAGES                                 │
│  ├─ Avis clients                                │
│  ├─ Notes 5 étoiles                             │
│  └─ Photos et citations                         │
└─────────────────────────────────────────────────┘
```

#### 📋 Services

<div align="center">

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  🔍 RECHERCHE │ --> │  🏷️ FILTRES  │ --> │  📋 RÉSULTATS│
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │                    │
       └────────────────────┴────────────────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │  📄 PAGE DÉTAIL  │
                   │  ├─ Description  │
                   │  ├─ Prix         │
                   │  └─ Durée        │
                   └─────────────────┘
```

</div>

#### 📰 Blog/CMS

```
┌──────────────────────────────────────────────┐
│  📝 ARTICLES                                 │
│  ├─ Titre                                    │
│  ├─ Auteur                                   │
│  ├─ Date                                     │
│  ├─ Catégorie                                │
│  ├─ Image mise en avant                      │
│  ├─ Contenu riche                            │
│  └─ Compteur de vues                         │
│                                              │
│  🏷️ CATÉGORIES                              │
│  ├─ Filtrage par catégorie                  │
│  ├─ Recherche                                │
│  └─ Pagination                               │
└──────────────────────────────────────────────┘
```

### 👤 Espace Client

<details>
<summary><b>📊 Schéma Dashboard Client - Cliquez pour voir</b></summary>

```mermaid
graph TD
    A[👤 Client Connecté] --> B[📊 Dashboard]
    B --> C[📝 Nouvelle Demande]
    B --> D[📋 Mes Demandes]
    B --> E[📥 Mes Livrables]
    B --> F[👤 Mon Profil]
    
    C --> G[📝 Formulaire]
    G --> H[✅ Demande Créée]
    
    D --> I[📊 Statut]
    D --> J[📅 Historique]
    D --> K[🔔 Notifications]
    
    E --> L[📄 Liste Fichiers]
    E --> M[⬇️ Téléchargement]
    
    style A fill:#0DE1E7
    style B fill:#0A1A2F,color:#fff
    style H fill:#28a745,color:#fff
```

</details>

#### 📊 Tableau Récapitulatif

| Fonctionnalité | Description | Statut |
|---------------|-------------|--------|
| 🎯 **Dashboard** | Vue d'ensemble personnalisée | ✅ |
| 📝 **Créer Demande** | Formulaire de demande de service | ✅ |
| 📋 **Mes Demandes** | Liste et suivi des demandes | ✅ |
| 📥 **Livrables** | Téléchargement des fichiers | ✅ |
| 👤 **Profil** | Gestion du compte utilisateur | ✅ |
| 🔔 **Notifications** | Alertes et mises à jour | ✅ |

### 🛡️ Espace Admin

<details>
<summary><b>📊 Schéma Dashboard Admin - Cliquez pour voir</b></summary>

```mermaid
graph TB
    A[⚙️ Admin Dashboard] --> B[📊 Statistiques]
    A --> C[👥 Utilisateurs]
    A --> D[💼 Services]
    A --> E[📝 Demandes]
    A --> F[📰 Blog]
    A --> G[🎫 Tickets]
    
    B --> H[📈 Graphiques]
    B --> I[📉 Métriques]
    
    C --> J[➕ Créer]
    C --> K[✏️ Modifier]
    C --> L[🗑️ Supprimer]
    
    D --> M[📦 Catégories]
    D --> N[🛍️ Services]
    
    E --> O[📋 Liste]
    E --> P[📄 Export PDF]
    E --> Q[📤 Livrables]
    
    style A fill:#0A1A2F,color:#fff
    style B fill:#0DE1E7
    style H fill:#28a745,color:#fff
```

</details>

#### 📊 Fonctionnalités Admin

```
┌──────────────────────────────────────────────────────────┐
│  📊 DASHBOARD PRINCIPAL                                   │
│  ├─ 📈 Statistiques en temps réel                        │
│  ├─ 📉 Graphiques Chart.js                               │
│  ├─ 📋 Demandes récentes                                 │
│  └─ ⚡ Actions rapides                                    │
│                                                          │
│  👥 GESTION UTILISATEURS                                 │
│  ├─ ➕ Création                                          │
│  ├─ ✏️ Modification                                     │
│  ├─ 🗑️ Suppression                                       │
│  ├─ 🔐 Gestion des rôles                                 │
│  └─ 📸 Gestion des avatars                               │
│                                                          │
│  💼 GESTION SERVICES                                    │
│  ├─ 📦 Catégories (CRUD)                                 │
│  ├─ 🛍️ Services (CRUD)                                   │
│  ├─ 💰 Prix et durées                                    │
│  └─ 🖼️ Images                                            │
│                                                          │
│  📝 GESTION DEMANDES                                     │
│  ├─ 📋 Liste complète                                    │
│  ├─ 👤 Assignation                                       │
│  ├─ 📊 Statuts et priorités                             │
│  ├─ 📄 Export PDF                                        │
│  └─ 📤 Gestion livrables                                 │
│                                                          │
│  📰 GESTION BLOG                                         │
│  ├─ 📝 Articles (CRUD)                                   │
│  ├─ 🏷️ Catégories                                        │
│  ├─ 🖼️ Images                                            │
│  └─ 📊 Statistiques                                      │
│                                                          │
│  🎫 GESTION TICKETS                                      │
│  ├─ 📋 Liste tickets                                     │
│  ├─ 💬 Messages                                         │
│  ├─ 👤 Assignation                                       │
│  └─ ✅ Résolution                                        │
└──────────────────────────────────────────────────────────┘
```

### 🤖 Chatbot IA Gemini

<details>
<summary><b>📊 Schéma Architecture Chatbot - Cliquez pour voir</b></summary>

```mermaid
sequenceDiagram
    participant U as 👤 Utilisateur
    participant F as 🌐 Frontend
    participant B as 🔵 Backend Django
    participant G as 🤖 Gemini AI
    
    U->>F: 💬 Tape un message
    F->>F: ✅ Validation CSRF
    F->>B: 📤 POST /chatbot/
    B->>B: 🔍 Validation JSON
    B->>B: 🔐 Vérification API Key
    B->>G: 🚀 Requête API Gemini
    G->>G: 🧠 Traitement IA
    G->>B: 📝 Réponse générée
    B->>B: 🛡️ Protection XSS
    B->>F: 📥 JSON Response
    F->>F: 🎨 Affichage message
    F->>U: 💬 Réponse affichée
```

</details>

#### 🔄 Flux du Chatbot

```
┌─────────────┐
│  👤 USER    │
└──────┬──────┘
       │ 💬 Message
       ▼
┌─────────────────┐
│  🎨 INTERFACE   │
│  ├─ Validation  │
│  └─ CSRF Token  │
└──────┬──────────┘
       │ POST /chatbot/
       ▼
┌─────────────────┐
│  🔵 DJANGO      │
│  ├─ Parse JSON  │
│  ├─ Validate    │
│  └─ Configure   │
└──────┬──────────┘
       │ API Call
       ▼
┌─────────────────┐
│  🤖 GEMINI AI   │
│  ├─ Process     │
│  └─ Generate    │
└──────┬──────────┘
       │ Response
       ▼
┌─────────────────┐
│  🔵 DJANGO      │
│  ├─ Sanitize    │
│  └─ Format      │
└──────┬──────────┘
       │ JSON
       ▼
┌─────────────────┐
│  🎨 INTERFACE   │
│  ├─ Display     │
│  └─ Animate     │
└──────┬──────────┘
       │ 💬 Réponse
       ▼
┌─────────────┐
│  👤 USER    │
└─────────────┘
```

#### 📊 Caractéristiques

| Fonctionnalité | Description | Statut |
|---------------|-------------|--------|
| 💬 **Interface Moderne** | Design animé et responsive | ✅ |
| 🧠 **IA Gemini** | Réponses intelligentes | ✅ |
| 🎯 **Contexte** | Personnalisé pour Uranus Group | ✅ |
| ⚡ **Performance** | Réponses rapides (gemini-2.5-flash) | ✅ |
| 🔒 **Sécurité** | CSRF, validation, XSS protection | ✅ |
| 📱 **Mobile** | Interface responsive | ✅ |

---

## 🛠️ Technologies

### 📊 Stack Technologique

<details>
<summary><b>📊 Schéma Architecture Technique - Cliquez pour voir</b></summary>

```mermaid
graph TB
    subgraph Frontend
        A[Tailwind CSS]
        B[GSAP]
        C[AOS]
        D[Chart.js]
        E[JavaScript ES6+]
    end
    
    subgraph Backend
        F[Django 5.0.1]
        G[DRF]
        H[Gunicorn]
    end
    
    subgraph Database
        I[PostgreSQL]
        J[SQLite Dev]
    end
    
    subgraph Cache
        K[Redis]
    end
    
    subgraph AI
        L[Gemini AI]
    end
    
    A --> F
    B --> F
    C --> F
    D --> F
    E --> F
    
    F --> G
    F --> I
    F --> J
    F --> K
    F --> L
    
    H --> F
    
    style F fill:#092E20,color:#fff
    style L fill:#4285F4,color:#fff
    style I fill:#316192,color:#fff
```

</details>

### 🔧 Backend

```
┌─────────────────────────────────────────┐
│  🔵 DJANGO 5.0.1                        │
│  ├─ Framework web principal            │
│  ├─ ORM pour base de données           │
│  ├─ Système d'authentification         │
│  └─ Admin interface                     │
│                                         │
│  🔌 DJANGO REST FRAMEWORK              │
│  ├─ API REST complète                   │
│  ├─ Serializers                         │
│  └─ ViewSets                            │
│                                         │
│  🗄️ BASE DE DONNÉES                    │
│  ├─ PostgreSQL (Production)            │
│  └─ SQLite (Développement)              │
│                                         │
│  ⚡ CACHE                               │
│  └─ Redis (Production)                  │
│                                         │
│  🚀 SERVEUR WSGI                        │
│  └─ Gunicorn                            │
└─────────────────────────────────────────┘
```

### 🎨 Frontend

```
┌─────────────────────────────────────────┐
│  🎨 TAILWIND CSS                        │
│  ├─ Framework CSS utilitaire            │
│  ├─ Design responsive                   │
│  └─ Personnalisation facile             │
│                                         │
│  ✨ GSAP 3.12.5                         │
│  ├─ Animations avancées                 │
│  ├─ ScrollTrigger                       │
│  └─ Timeline                            │
│                                         │
│  📊 CHART.JS                            │
│  ├─ Graphiques interactifs              │
│  ├─ Statistiques                        │
│  └─ Visualisations                      │
│                                         │
│  🎭 AOS                                 │
│  └─ Animations au scroll                │
└─────────────────────────────────────────┘
```

### 🤖 IA & Outils

```
┌─────────────────────────────────────────┐
│  🤖 GOOGLE GEMINI AI                    │
│  ├─ Modèle: gemini-2.5-flash           │
│  ├─ Réponses intelligentes              │
│  └─ Contexte personnalisé               │
│                                         │
│  📄 REPORTLAB                           │
│  └─ Génération PDF                      │
│                                         │
│  🖼️ PILLOW                              │
│  └─ Traitement d'images                 │
│                                         │
│  🔐 PYTHON-DECOUPLE                     │
│  └─ Variables d'environnement           │
└─────────────────────────────────────────┘
```

---

## 🚀 Installation

### 📊 Schéma d'Installation

<details>
<summary><b>📊 Processus d'Installation - Cliquez pour voir</b></summary>

```mermaid
flowchart TD
    A[📥 Cloner Projet] --> B[🐍 Créer venv]
    B --> C[📦 Installer Dépendances]
    C --> D[🗄️ Migrations]
    D --> E[👤 Superuser]
    E --> F[📁 Collectstatic]
    F --> G[🚀 Runserver]
    G --> H[✅ Prêt!]
    
    style A fill:#0DE1E7
    style H fill:#28a745,color:#fff
```

</details>

### 🔧 Étapes Détaillées

<div style="background: #0A1A2F; color: #0DE1E7; padding: 20px; border-radius: 10px; margin: 20px 0;">

```bash
# ┌─────────────────────────────────────────┐
# │  ÉTAPE 1: PRÉPARATION                   │
# └─────────────────────────────────────────┘
cd /home/maxime/newC_uranusgroup_V

# ┌─────────────────────────────────────────┐
# │  ÉTAPE 2: ENVIRONNEMENT VIRTUEL        │
# └─────────────────────────────────────────┘
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# ┌─────────────────────────────────────────┐
# │  ÉTAPE 3: DÉPENDANCES                   │
# └─────────────────────────────────────────┘
pip install -r requirements.txt

# ┌─────────────────────────────────────────┐
# │  ÉTAPE 4: BASE DE DONNÉES               │
# └─────────────────────────────────────────┘
python manage.py makemigrations
python manage.py migrate

# ┌─────────────────────────────────────────┐
# │  ÉTAPE 5: SUPERUTILISATEUR              │
# └─────────────────────────────────────────┘
python manage.py createsuperuser

# ┌─────────────────────────────────────────┐
# │  ÉTAPE 6: FICHIERS STATIQUES           │
# └─────────────────────────────────────────┘
python manage.py collectstatic --noinput

# ┌─────────────────────────────────────────┐
# │  ÉTAPE 7: LANCER LE SERVEUR             │
# └─────────────────────────────────────────┘
python manage.py runserver
```

</div>

### 🎯 Accès

```
┌─────────────────────────────────────────────┐
│  🌐 URLS D'ACCÈS                            │
├─────────────────────────────────────────────┤
│  Site web:      http://127.0.0.1:8000/     │
│  Admin Django:  http://127.0.0.1:8000/admin/│
│  Dashboard:     http://127.0.0.1:8000/      │
│                dashboard/admin/             │
│  API REST:      http://127.0.0.1:8000/api/ │
│  Health Check: http://127.0.0.1:8000/      │
│                health/                      │
└─────────────────────────────────────────────┘
```

---

## ⚙️ Configuration

### 🔑 Variables d'Environnement

<details>
<summary><b>📊 Schéma Configuration - Cliquez pour voir</b></summary>

```mermaid
graph LR
    A[.env File] --> B[Settings.py]
    B --> C[Application]
    
    A --> D[SECRET_KEY]
    A --> E[DEBUG]
    A --> F[DATABASE]
    A --> G[EMAIL]
    A --> H[GEMINI_API]
    
    style A fill:#0DE1E7
    style B fill:#0A1A2F,color:#fff
```

</details>

#### 📝 Fichier .env

```
┌─────────────────────────────────────────────────┐
│  🔐 SÉCURITÉ                                    │
│  SECRET_KEY=votre-clé-secrète                  │
│  DEBUG=True                                     │
│  ALLOWED_HOSTS=localhost,127.0.0.1             │
│                                                 │
│  🗄️ BASE DE DONNÉES (Production)               │
│  DB_NAME=uranusgroup                           │
│  DB_USER=postgres                               │
│  DB_PASSWORD=votre-mot-de-passe                │
│  DB_HOST=localhost                              │
│  DB_PORT=5432                                   │
│                                                 │
│  📧 EMAIL                                       │
│  EMAIL_HOST=smtp.gmail.com                     │
│  EMAIL_PORT=587                                 │
│  EMAIL_USE_TLS=True                            │
│  EMAIL_HOST_USER=votre-email@gmail.com         │
│  EMAIL_HOST_PASSWORD=votre-mot-de-passe-app    │
│                                                 │
│  🤖 GEMINI AI                                   │
│  GEMINI_API_KEY=votre-clé-api-gemini           │
│                                                 │
│  ⚡ REDIS (Production)                          │
│  REDIS_URL=redis://127.0.0.1:6379/1            │
└─────────────────────────────────────────────────┘
```

---

## 🔒 Sécurité

### 🛡️ Schéma de Protection

<details>
<summary><b>📊 Architecture de Sécurité - Cliquez pour voir</b></summary>

```mermaid
graph TB
    A[🌐 Requête] --> B{🔐 Authentification}
    B -->|✅ Authentifié| C{🛡️ Autorisation}
    B -->|❌ Non| D[🚫 Accès Refusé]
    
    C -->|✅ Autorisé| E[✅ Accès Autorisé]
    C -->|❌ Non| D
    
    E --> F[🛡️ Protection CSRF]
    E --> G[🛡️ Protection XSS]
    E --> H[🛡️ Protection SQL]
    
    F --> I[📝 Validation]
    G --> I
    H --> I
    
    I --> J[✅ Réponse Sécurisée]
    
    style A fill:#0DE1E7
    style D fill:#dc3545,color:#fff
    style J fill:#28a745,color:#fff
```

</details>

### 📊 Tableau de Protection

| Protection | Méthode | Statut | Description |
|-----------|---------|--------|-------------|
| 🔐 **CSRF** | Middleware Django | ✅ | Tokens sur tous les formulaires |
| 🛡️ **XSS** | Échappement auto | ✅ | Templates Django sécurisés |
| 💉 **SQL Injection** | ORM Django | ✅ | Requêtes paramétrées |
| 🔒 **Authentification** | Django Auth | ✅ | Hashage bcrypt |
| 👮 **Autorisation** | Système de rôles | ✅ | Permissions granulaires |
| 🍪 **Sessions** | Cookies sécurisés | ✅ | HttpOnly, Secure |

### 🧪 Tests de Sécurité

```
┌─────────────────────────────────────────┐
│  🔍 TESTS DISPONIBLES                   │
├─────────────────────────────────────────┤
│  ✅ Audit de configuration              │
│  ✅ Tests de pénétration                │
│  ✅ Tests chatbot                       │
│  ✅ Tests CSRF                          │
│  ✅ Tests XSS                           │
│  ✅ Tests SQL Injection                 │
│  ✅ Tests authentification              │
└─────────────────────────────────────────┘

📊 Score Global: 75% ✅
```

---

## 📊 Architecture

### 🏗️ Structure du Projet

<details>
<summary><b>📊 Arborescence Complète - Cliquez pour voir</b></summary>

```mermaid
graph TD
    A[uranusgroup/] --> B[accounts/]
    A --> C[blog/]
    A --> D[core/]
    A --> E[dashboard/]
    A --> F[services/]
    A --> G[templates/]
    A --> H[static/]
    A --> I[media/]
    A --> J[uranusgroup/]
    
    B --> B1[models.py]
    B --> B2[views.py]
    B --> B3[urls.py]
    
    D --> D1[chatbot view]
    D --> D2[home view]
    D --> D3[contact view]
    
    F --> F1[api.py]
    F --> F2[models.py]
    F --> F3[serializers.py]
    
    style A fill:#0A1A2F,color:#fff
    style D fill:#0DE1E7
    style F fill:#4285F4,color:#fff
```

</details>

### 📁 Structure Détaillée

```
uranusgroup/
│
├── 📂 accounts/              # 👤 Gestion utilisateurs
│   ├── models.py            # User, UserProfile
│   ├── views.py             # Auth, profil
│   └── urls.py
│
├── 📂 blog/                  # 📰 Blog/CMS
│   ├── models.py            # Article, Category
│   ├── views.py
│   └── urls.py
│
├── 📂 core/                  # 🏠 Pages principales
│   ├── models.py            # Contact, Team, Slider
│   ├── views.py             # Home, contact, chatbot
│   └── urls.py
│
├── 📂 dashboard/             # 🛡️ Dashboard admin
│   ├── models.py            # Notification, Ticket
│   ├── views.py             # Vues admin
│   └── urls.py
│
├── 📂 services/              # 💼 Services QHSE/Info
│   ├── models.py            # Service, Request, Deliverable
│   ├── api.py               # API REST
│   ├── serializers.py
│   └── urls.py
│
├── 📂 templates/             # 🎨 Templates HTML
│   ├── base.html
│   ├── accounts/
│   ├── blog/
│   ├── core/
│   ├── dashboard/
│   └── services/
│
├── 📂 static/                # 🎨 Fichiers statiques
│   ├── css/
│   ├── js/
│   └── images/
│
└── 📂 uranusgroup/           # ⚙️ Configuration
    ├── settings.py
    ├── settings_production.py
    └── urls.py
```

### 🔄 Flux de Données

<details>
<summary><b>📊 Flux Complet - Cliquez pour voir</b></summary>

```mermaid
sequenceDiagram
    participant U as Utilisateur
    participant B as Browser
    participant D as Django
    participant DB as Database
    participant AI as Gemini AI
    
    U->>B: Requête HTTP
    B->>D: Requête Django
    D->>D: Middleware (CSRF, Auth)
    D->>DB: Query ORM
    DB->>D: Données
    D->>D: Template Rendering
    D->>B: HTML Response
    B->>U: Page Affichée
    
    Note over U,AI: Chatbot Flow
    U->>B: Message Chatbot
    B->>D: POST /chatbot/
    D->>AI: API Gemini
    AI->>D: Réponse IA
    D->>B: JSON Response
    B->>U: Message Affiché
```

</details>

---

## 🌐 Déploiement

### 🚀 Processus de Déploiement

<details>
<summary><b>📊 Schéma Déploiement - Cliquez pour voir</b></summary>

```mermaid
graph LR
    A[Code] --> B[Tests]
    B --> C[Build]
    C --> D[Deploy]
    D --> E[Production]
    
    E --> F[Nginx]
    E --> G[Gunicorn]
    E --> H[PostgreSQL]
    E --> I[Redis]
    
    style A fill:#0DE1E7
    style E fill:#28a745,color:#fff
```

</details>

### 📋 Checklist

```
┌─────────────────────────────────────────┐
│  ✅ CHECKLIST DÉPLOIEMENT               │
├─────────────────────────────────────────┤
│  [ ] Générer SECRET_KEY                 │
│  [ ] DEBUG = False                      │
│  [ ] Configurer ALLOWED_HOSTS           │
│  [ ] Configurer PostgreSQL              │
│  [ ] Configurer Redis                   │
│  [ ] Configurer SMTP                    │
│  [ ] Configurer Gemini API              │
│  [ ] Collectstatic                      │
│  [ ] Configurer Nginx                   │
│  [ ] Configurer Gunicorn                │
│  [ ] Obtenir SSL                        │
│  [ ] Tests de sécurité                  │
│  [ ] Backup                             │
└─────────────────────────────────────────┘
```

---

## 🧪 Tests

### 📊 Schéma de Tests

<details>
<summary><b>📊 Architecture Tests - Cliquez pour voir</b></summary>

```mermaid
graph TB
    A[Tests] --> B[Security Tests]
    A --> C[Unit Tests]
    A --> D[Integration Tests]
    
    B --> E[Audit]
    B --> F[Penetration]
    B --> G[Chatbot Security]
    
    C --> H[Models]
    C --> I[Views]
    C --> J[API]
    
    D --> K[Workflows]
    D --> L[End-to-End]
    
    style A fill:#0DE1E7
    style B fill:#dc3545,color:#fff
    style C fill:#ffc107
    style D fill:#28a745,color:#fff
```

</details>

### 🧪 Commandes de Test

```
┌─────────────────────────────────────────┐
│  🔍 TESTS DE SÉCURITÉ                   │
├─────────────────────────────────────────┤
│  ./run_full_pentest.sh                  │
│  python security_audit.py               │
│  python security_tests.py               │
│  python chatbot_security_tests.py       │
│                                         │
│  ✅ TESTS DJANGO                        │
│  python manage.py test                  │
│  python manage.py test accounts        │
│  python manage.py test services         │
└─────────────────────────────────────────┘
```

---

## 📚 Documentation

### 📄 Documents Disponibles

```
┌─────────────────────────────────────────┐
│  📚 DOCUMENTATION                       │
├─────────────────────────────────────────┤
│  📊 ANALYSE_PROJET.md                   │
│  🔒 PENTEST_REPORT.md                   │
│  🚀 DEPLOYMENT.md                       │
│  ✅ PRODUCTION_CHECKLIST.md             │
│  🤖 CHATBOT_README.md                   │
│  🛡️ ADMIN_FEATURES.md                   │
│  🔐 SECURITY_SUMMARY.md                 │
└─────────────────────────────────────────┘
```

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
