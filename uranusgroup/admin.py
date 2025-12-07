"""
Configuration de l'administration Django personnalisée pour Uranus Group.
"""
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Désenregistrer les modèles par défaut
admin.site.unregister(Group)
admin.site.unregister(User)

# Personnalisation du site admin
admin.site.site_header = 'Administration Uranus Group'
admin.site.site_title = 'Uranus Group Admin'
admin.site.index_title = 'Tableau de bord'

# Personnalisation de l'admin utilisateur
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    actions = ['delete_selected']
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' not in actions:
            return actions
        return actions

# Importer les configurations d'admin des applications
from services.admin import *
from blog.admin import *
from accounts.admin import *
from dashboard.admin import *
from core.admin import *
