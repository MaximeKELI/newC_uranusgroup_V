"""
Models pour la gestion des services QHSE et Informatique
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ServiceCategory(models.Model):
    """
    Catégorie de service (QHSE ou Informatique)
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Description")
    icon = models.CharField(max_length=50, blank=True, verbose_name="Icône")
    color = models.CharField(max_length=7, default="#0DE1E7", verbose_name="Couleur")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    
    class Meta:
        verbose_name = "Catégorie de service"
        verbose_name_plural = "Catégories de services"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Service(models.Model):
    """
    Service proposé par Uranus Group
    """
    STATUS_CHOICES = [
        ('active', 'Actif'),
        ('inactive', 'Inactif'),
    ]
    
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name="Catégorie"
    )
    name = models.CharField(max_length=200, verbose_name="Nom")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    short_description = models.TextField(verbose_name="Description courte")
    full_description = models.TextField(verbose_name="Description complète")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Image")
    icon = models.CharField(max_length=50, blank=True, verbose_name="Icône")
    price_starting_from = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Prix à partir de"
    )
    duration = models.CharField(max_length=50, blank=True, verbose_name="Durée")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Statut"
    )
    featured = models.BooleanField(default=False, verbose_name="Mis en avant")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class ServiceRequest(models.Model):
    """
    Demande de service par un client
    """
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Basse'),
        ('medium', 'Moyenne'),
        ('high', 'Haute'),
        ('urgent', 'Urgente'),
    ]
    
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='requests',
        verbose_name="Service"
    )
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='service_requests',
        verbose_name="Client"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_requests',
        verbose_name="Assigné à"
    )
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Statut"
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name="Priorité"
    )
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Date limite")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Date de complétion")
    
    class Meta:
        verbose_name = "Demande de service"
        verbose_name_plural = "Demandes de services"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.client.username}"


class Deliverable(models.Model):
    """
    Livrable associé à une demande de service
    """
    request = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE,
        related_name='deliverables',
        verbose_name="Demande"
    )
    name = models.CharField(max_length=200, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")
    file = models.FileField(upload_to='deliverables/', verbose_name="Fichier")
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='uploaded_deliverables',
        verbose_name="Uploadé par"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'upload")
    
    class Meta:
        verbose_name = "Livrable"
        verbose_name_plural = "Livrables"
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.name} - {self.request.title}"


class Certification(models.Model):
    """
    Certifications ISO et autres
    """
    name = models.CharField(max_length=200, verbose_name="Nom")
    code = models.CharField(max_length=50, unique=True, verbose_name="Code (ex: ISO 9001)")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='certifications/', blank=True, null=True, verbose_name="Image")
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='certifications',
        verbose_name="Catégorie"
    )
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Testimonial(models.Model):
    """
    Témoignages clients
    """
    client_name = models.CharField(max_length=200, verbose_name="Nom du client")
    client_position = models.CharField(max_length=200, blank=True, verbose_name="Poste")
    client_company = models.CharField(max_length=200, blank=True, verbose_name="Entreprise")
    client_avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True, verbose_name="Photo")
    content = models.TextField(verbose_name="Contenu")
    rating = models.IntegerField(default=5, verbose_name="Note (1-5)")
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='testimonials',
        verbose_name="Service"
    )
    featured = models.BooleanField(default=False, verbose_name="Mis en avant")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    
    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f"Témoignage de {self.client_name}"
