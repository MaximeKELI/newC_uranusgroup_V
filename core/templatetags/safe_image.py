"""
Filtre pour accéder de manière sécurisée aux URLs d'images
"""
from django import template

register = template.Library()


@register.filter
def safe_url(field):
    """Retourne l'URL d'un champ image de manière sécurisée"""
    if not field:
        return None
    try:
        return field.url
    except (ValueError, AttributeError):
        return None

