"""
Filtres personnalisés pour les images
"""
from django import template

register = template.Library()


@register.filter
def has_file(field):
    """Vérifie si un champ ImageField/FileField a un fichier"""
    if not field:
        return False
    try:
        return bool(field.name) and field.storage.exists(field.name)
    except (ValueError, AttributeError):
        return False

