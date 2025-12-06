"""
Models pour l'app core (contact, à propos, etc.)
"""
from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    """
    Messages de contact depuis le formulaire
    """
    STATUS_CHOICES = [
        ('new', 'Nouveau'),
        ('read', 'Lu'),
        ('replied', 'Répondu'),
        ('archived', 'Archivé'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Nom")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    company = models.CharField(max_length=200, blank=True, verbose_name="Entreprise")
    subject = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="Statut"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    replied_at = models.DateTimeField(null=True, blank=True, verbose_name="Date de réponse")
    
    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.subject} - {self.name}"


class TeamMember(models.Model):
    """
    Membres de l'équipe pour la page À propos
    """
    name = models.CharField(max_length=200, verbose_name="Nom")
    position = models.CharField(max_length=200, verbose_name="Poste")
    bio = models.TextField(blank=True, verbose_name="Biographie")
    photo = models.ImageField(upload_to='team/', blank=True, null=True, verbose_name="Photo")
    email = models.EmailField(blank=True, verbose_name="Email")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Membre de l'équipe"
        verbose_name_plural = "Membres de l'équipe"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.position}"


class SliderItem(models.Model):
    """
    Items du slider de la landing page
    """
    title = models.CharField(max_length=200, verbose_name="Titre")
    subtitle = models.CharField(max_length=300, blank=True, verbose_name="Sous-titre")
    description = models.TextField(blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='slider/', verbose_name="Image")
    button_text = models.CharField(max_length=50, blank=True, verbose_name="Texte du bouton")
    button_link = models.CharField(max_length=200, blank=True, verbose_name="Lien du bouton")
    active = models.BooleanField(default=True, verbose_name="Actif")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Item du slider"
        verbose_name_plural = "Items du slider"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
