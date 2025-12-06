# Guide de Personnalisation - Uranus Group

Ce guide vous explique comment personnaliser le contenu de votre site web.

## 📧 Configuration Email

### Pour Gmail

1. Activez l'authentification à deux facteurs sur votre compte Gmail
2. Générez un mot de passe d'application :
   - Allez dans votre compte Google > Sécurité
   - Sous "Connexion à Google", cliquez sur "Mots de passe des applications"
   - Créez un nouveau mot de passe d'application
3. Modifiez `uranusgroup/settings.py` :

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "votre-email@gmail.com"
EMAIL_HOST_PASSWORD = "votre-mot-de-passe-app"
DEFAULT_FROM_EMAIL = "noreply@uranusgroup.com"
```

### Pour SendGrid

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = "votre-api-key-sendgrid"
DEFAULT_FROM_EMAIL = "noreply@uranusgroup.com"
```

### Pour Mailgun

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "postmaster@votre-domaine.mailgun.org"
EMAIL_HOST_PASSWORD = "votre-mot-de-passe-mailgun"
DEFAULT_FROM_EMAIL = "noreply@uranusgroup.com"
```

## 🎨 Personnalisation des Contenus

### 1. Modifier les Informations de Contact

Éditez le template `templates/core/contact.html` pour modifier :
- L'adresse email
- Le numéro de téléphone
- L'adresse physique
- Les horaires d'ouverture

### 2. Ajouter/Modifier des Services

Via l'admin Django (`/admin/`) :
1. Connectez-vous avec le compte admin
2. Allez dans "Services" > "Services"
3. Cliquez sur "Ajouter un service"
4. Remplissez les champs :
   - Nom, slug, descriptions
   - Catégorie (QHSE ou Informatique)
   - Prix, durée
   - Image (optionnel)
   - Icône Font Awesome (ex: `fas fa-certificate`)

### 3. Ajouter des Articles de Blog

1. Allez dans "Blog" > "Articles"
2. Cliquez sur "Ajouter un article"
3. Remplissez :
   - Titre, slug, extrait, contenu
   - Catégorie
   - Image mise en avant
   - Statut : "Publié" pour afficher l'article

### 4. Modifier le Slider de la Page d'Accueil

1. Allez dans "Core" > "Items du slider"
2. Ajoutez/modifiez les slides :
   - Titre, sous-titre, description
   - Image (1920x1080px recommandé)
   - Texte et lien du bouton
   - Ordre d'affichage

### 5. Ajouter des Membres de l'Équipe

1. Allez dans "Core" > "Membres de l'équipe"
2. Ajoutez les membres :
   - Nom, poste, biographie
   - Photo (carrée, 400x400px recommandé)
   - Email, LinkedIn (optionnel)
   - Ordre d'affichage

### 6. Ajouter des Certifications

1. Allez dans "Services" > "Certifications"
2. Ajoutez les certifications :
   - Nom, code (ex: ISO 9001)
   - Description
   - Image du logo
   - Catégorie
   - Ordre d'affichage

### 7. Ajouter des Témoignages

1. Allez dans "Services" > "Témoignages"
2. Ajoutez un témoignage :
   - Nom du client, poste, entreprise
   - Photo (optionnel)
   - Contenu du témoignage
   - Note (1-5 étoiles)
   - Service associé (optionnel)
   - Cochez "Mis en avant" pour l'afficher sur la page d'accueil

## 🎨 Personnalisation du Design

### Modifier les Couleurs

Éditez `templates/base.html` et modifiez les variables CSS :

```css
:root {
    --primary-dark: #0A1A2F;  /* Couleur principale foncée */
    --primary-cyan: #0DE1E7;  /* Couleur principale cyan */
    --white: #FFFFFF;          /* Blanc */
}
```

### Modifier la Typographie

Dans `templates/base.html`, modifiez la propriété `font-family` :

```css
body {
    font-family: 'Votre Police', -apple-system, BlinkMacSystemFont, sans-serif;
}
```

Pour ajouter une police Google Fonts, ajoutez dans le `<head>` :

```html
<link href="https://fonts.googleapis.com/css2?family=VotrePolice&display=swap" rel="stylesheet">
```

## 🔧 Configuration Avancée

### Changer le Nom de l'Entreprise

Recherchez et remplacez "Uranus Group" dans :
- `templates/base.html` (navigation, footer)
- `templates/core/home.html`
- `templates/core/about.html`
- `templates/core/contact.html`

### Modifier le Logo

Remplacez l'icône dans `templates/base.html` :

```html
<a href="{% url 'core:home' %}" class="text-2xl font-bold text-primary-cyan">
    <img src="{% static 'images/logo.png' %}" alt="Uranus Group" class="h-10">
</a>
```

Puis ajoutez votre logo dans `static/images/logo.png`

### Ajouter des Pages Personnalisées

1. Créez une nouvelle vue dans `core/views.py` :

```python
def ma_page(request):
    return render(request, 'core/ma_page.html')
```

2. Ajoutez l'URL dans `core/urls.py` :

```python
path('ma-page/', views.ma_page, name='ma_page'),
```

3. Créez le template `templates/core/ma_page.html`

## 📱 Personnalisation Mobile

Le site est déjà responsive grâce à Tailwind CSS. Pour ajuster :
- Modifiez les classes `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` selon vos besoins
- Ajustez les espacements avec les classes `py-*`, `px-*`, `mb-*`, etc.

## 🔐 Sécurité en Production

Avant de mettre en production :

1. **Changez le SECRET_KEY** :
   ```python
   SECRET_KEY = "générez-une-clé-secrète-aléatoire"
   ```

2. **Désactivez DEBUG** :
   ```python
   DEBUG = False
   ```

3. **Configurez ALLOWED_HOSTS** :
   ```python
   ALLOWED_HOSTS = ['votre-domaine.com', 'www.votre-domaine.com']
   ```

4. **Utilisez une base de données PostgreSQL** :
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'uranusgroup',
           'USER': 'votre-user',
           'PASSWORD': 'votre-password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Configurez les fichiers statiques** avec un serveur web (Nginx, Apache)

6. **Utilisez HTTPS** avec un certificat SSL

## 📝 Notes Importantes

- Les images uploadées sont stockées dans `media/`
- Les fichiers statiques sont dans `static/`
- Sauvegardez régulièrement votre base de données
- Testez toujours en local avant de déployer en production

## 🆘 Support

Pour toute question ou problème, consultez :
- La documentation Django : https://docs.djangoproject.com/
- La documentation Tailwind CSS : https://tailwindcss.com/docs

