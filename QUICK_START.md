# Guide de Démarrage Rapide - Uranus Group

## 🚀 Démarrage Immédiat

### 1. Activer l'environnement virtuel

```bash
cd /home/maxime/newC_uranusgroup_V
source venv/bin/activate
```

### 2. Lancer le serveur

```bash
python manage.py runserver
```

Le site sera accessible sur : **http://127.0.0.1:8000/**

### 3. Accéder à l'admin Django

URL : **http://127.0.0.1:8000/admin/**

**Identifiants par défaut :**
- Username : `admin`
- Password : `admin123`

⚠️ **IMPORTANT** : Changez le mot de passe immédiatement !

## 📊 Données de Test Créées

Les données suivantes ont été automatiquement créées :

### Services
- **QHSE** : 5 services (ISO 9001, 14001, 45001, 22000, 27001)
- **Informatique** : 4 services (Audit cybersécurité, IA, Développement, Formation)

### Autres
- 5 certifications ISO
- 3 témoignages clients
- 2 articles de blog
- 3 items de slider
- 3 membres de l'équipe

## 🎯 Prochaines Étapes

### 1. Personnaliser le Contenu

- Connectez-vous à l'admin Django
- Modifiez les services, articles, témoignages selon vos besoins
- Ajoutez vos propres images dans les médias

### 2. Configurer l'Email

Éditez `uranusgroup/settings.py` et configurez les paramètres SMTP (voir `GUIDE_PERSONNALISATION.md`)

### 3. Personnaliser le Design

- Modifiez les couleurs dans `templates/base.html`
- Ajoutez votre logo
- Personnalisez les textes

### 4. Créer des Utilisateurs

Via l'admin Django :
- Créez des utilisateurs avec différents rôles
- Testez les permissions selon les rôles

## 🔑 Rôles Disponibles

- **admin** : Accès complet à tout
- **manager_qhse** : Gestion des services QHSE
- **manager_info** : Gestion des services Informatique
- **client** : Création de demandes, consultation de ses livrables

## 📁 Structure Importante

```
uranusgroup/
├── templates/          # Templates HTML
├── static/            # CSS, JS, images statiques
├── media/             # Fichiers uploadés (créé automatiquement)
├── uranusgroup/       # Configuration
│   └── settings.py    # Configuration principale
└── manage.py          # Script de gestion Django
```

## 🛠️ Commandes Utiles

### Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### Créer les données de test
```bash
python create_test_data.py
```

### Appliquer les migrations
```bash
python manage.py migrate
```

### Collecter les fichiers statiques
```bash
python manage.py collectstatic
```

### Accéder au shell Django
```bash
python manage.py shell
```

## 📚 Documentation Complète

Consultez `GUIDE_PERSONNALISATION.md` pour :
- Configuration email détaillée
- Personnalisation avancée
- Guide de déploiement
- Sécurité en production

## ✅ Checklist de Démarrage

- [x] Environnement virtuel activé
- [x] Serveur lancé
- [x] Accès à l'admin Django
- [x] Données de test créées
- [ ] Mot de passe admin changé
- [ ] Contenus personnalisés
- [ ] Email configuré
- [ ] Logo et design personnalisés

## 🎉 C'est Prêt !

Votre site Uranus Group est maintenant opérationnel. Commencez à personnaliser les contenus via l'admin Django !

