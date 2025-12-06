"""
Models pour la gestion des utilisateurs et authentification
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Modèle utilisateur personnalisé avec gestion des rôles
    """
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('manager_qhse', 'Manager QHSE'),
        ('manager_info', 'Manager Informatique'),
        ('client', 'Client'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='client',
        verbose_name="Rôle"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    company = models.CharField(max_length=200, blank=True, verbose_name="Entreprise")
    position = models.CharField(max_length=200, blank=True, verbose_name="Poste")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Photo de profil")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    is_verified = models.BooleanField(default=False, verbose_name="Compte vérifié")
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser
    
    def is_manager_qhse(self):
        return self.role == 'manager_qhse'
    
    def is_manager_info(self):
        return self.role == 'manager_info'
    
    def is_client(self):
        return self.role == 'client'


class UserProfile(models.Model):
    """
    Profil étendu pour les utilisateurs
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, verbose_name="Biographie")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    website = models.URLField(blank=True, verbose_name="Site web")
    
    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name_plural = "Profils utilisateurs"
    
    def __str__(self):
        return f"Profil de {self.user.username}"
