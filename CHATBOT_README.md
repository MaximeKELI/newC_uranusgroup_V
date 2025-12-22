# 🤖 Chatbot IA Gemini - Uranus Group

## 📋 Description

Un chatbot intelligent intégré au site Uranus Group utilisant l'API Google Gemini. Le chatbot est accessible sur toutes les pages du site via un bouton flottant et permet aux visiteurs d'obtenir des informations sur les services QHSE et Informatique.

## ✨ Fonctionnalités

- **Interface moderne et responsive** avec animations fluides
- **Réponses intelligentes** générées par l'IA Gemini
- **Contexte personnalisé** pour Uranus Group (QHSE et Informatique)
- **Indicateur de frappe** pour une meilleure expérience utilisateur
- **Historique de conversation** dans la session
- **Design cohérent** avec les couleurs du site (#0A1A2F et #0DE1E7)

## 🚀 Installation

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

La bibliothèque `google-generativeai==0.3.2` a été ajoutée aux dépendances.

### 2. Configuration de la clé API

La clé API Gemini est configurée dans `uranusgroup/settings.py` :

```python
GEMINI_API_KEY = config('GEMINI_API_KEY', default='AIzaSyAoAnErMdEP7OYtoaDemWPYrN9NydF3Tj4')
```

**⚠️ Important pour la production :** 
Pour plus de sécurité, il est recommandé de mettre la clé API dans un fichier `.env` :

```bash
# .env
GEMINI_API_KEY=AIzaSyAoAnErMdEP7OYtoaDemWPYrN9NydF3Tj4
```

### 3. Collecter les fichiers statiques

```bash
python manage.py collectstatic --noinput
```

## 📁 Fichiers Créés/Modifiés

### Nouveaux fichiers

- `static/js/chatbot.js` - Logique JavaScript du chatbot
- `static/css/chatbot.css` - Styles CSS du chatbot

### Fichiers modifiés

- `core/views.py` - Ajout de la vue `chatbot()`
- `core/urls.py` - Ajout de la route `/chatbot/`
- `templates/base.html` - Intégration du chatbot
- `uranusgroup/settings.py` - Configuration de la clé API Gemini
- `requirements.txt` - Ajout de `google-generativeai`

## 🎨 Interface Utilisateur

### Bouton flottant

Un bouton flottant avec animation de pulsation apparaît en bas à droite de toutes les pages. Il permet d'ouvrir/fermer le chatbot.

### Fenêtre du chatbot

- **Header** : Avatar du bot, nom "Assistant Uranus Group", statut "En ligne"
- **Zone de messages** : Affichage des messages utilisateur et bot avec bulles différenciées
- **Zone de saisie** : Champ de texte avec bouton d'envoi

### Design

- **Couleurs** : Utilise les couleurs principales du site (cyan #0DE1E7 et dark #0A1A2F)
- **Animations** : Transitions fluides, indicateur de frappe animé
- **Responsive** : S'adapte aux écrans mobiles

## 🔧 Configuration

### Personnaliser le prompt système

Le prompt système qui contextualise le chatbot se trouve dans `core/views.py` :

```python
system_prompt = """Tu es un assistant virtuel pour Uranus Group...
"""
```

Vous pouvez modifier ce prompt pour adapter les réponses du chatbot à vos besoins.

### Modifier les styles

Les styles CSS sont dans `static/css/chatbot.css`. Vous pouvez personnaliser :
- Les couleurs
- La taille de la fenêtre
- Les animations
- Le positionnement

## 📡 API Endpoint

### POST `/chatbot/`

**Requête :**
```json
{
    "message": "Bonjour, quels services proposez-vous ?"
}
```

**Réponse (succès) :**
```json
{
    "response": "Bonjour ! Uranus Group propose des services en QHSE...",
    "status": "success"
}
```

**Réponse (erreur) :**
```json
{
    "error": "Erreur lors de la génération de la réponse: ...",
    "status": "error"
}
```

## 🔒 Sécurité

- **Protection CSRF** : Le token CSRF est automatiquement inclus dans les requêtes
- **Validation** : Les messages vides sont rejetés
- **Gestion d'erreurs** : Les erreurs sont gérées proprement côté serveur et client

## 🐛 Dépannage

### Le chatbot ne s'affiche pas

1. Vérifiez que les fichiers statiques sont collectés : `python manage.py collectstatic`
2. Vérifiez la console du navigateur pour les erreurs JavaScript
3. Assurez-vous que `chatbot.js` et `chatbot.css` sont bien chargés dans `base.html`

### Erreur "API key not valid"

1. Vérifiez que la clé API Gemini est correcte dans `settings.py`
2. Vérifiez que la clé API a les permissions nécessaires
3. Consultez les logs Django pour plus de détails

### Le chatbot ne répond pas

1. Vérifiez la connexion internet (nécessaire pour l'API Gemini)
2. Vérifiez les logs Django pour les erreurs serveur
3. Vérifiez que l'endpoint `/chatbot/` est accessible

## 📝 Notes

- Le chatbot utilise le modèle `gemini-pro` de Google
- Les réponses sont générées en temps réel via l'API Gemini
- Le chatbot est disponible sur toutes les pages du site
- L'historique de conversation n'est pas persisté (seulement dans la session navigateur)

## 🔄 Mises à jour futures possibles

- Persistance de l'historique de conversation
- Support de fichiers/images dans les messages
- Intégration avec la base de données pour des réponses plus précises
- Analytics des questions les plus fréquentes
- Mode sombre/clair

---

*Chatbot créé le 6 décembre 2024*


