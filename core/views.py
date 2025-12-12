"""
Vues pour l'app core (home, contact, à propos)
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_http_methods
from .models import ContactMessage, TeamMember, SliderItem
from services.models import Service, ServiceCategory, Certification, Testimonial


def home(request):
    """
    Landing page avec slider, sections QHSE/Informatique, certifications, témoignages
    """
    slider_items = SliderItem.objects.filter(active=True).order_by('order')
    qhse_category = ServiceCategory.objects.filter(slug='qhse', is_active=True).first()
    info_category = ServiceCategory.objects.filter(slug='informatique', is_active=True).first()
    
    # Récupérer les services et convertir en liste pour éviter les problèmes de QuerySet vide
    if qhse_category:
        qhse_services_qs = Service.objects.filter(category=qhse_category, status='active', is_active=True).order_by('order')[:6]
        qhse_services = list(qhse_services_qs)
    else:
        qhse_services = []
    
    if info_category:
        info_services_qs = Service.objects.filter(category=info_category, status='active', is_active=True).order_by('order')[:6]
        info_services = list(info_services_qs)
    else:
        info_services = []
    
    certifications = Certification.objects.all().order_by('order')[:8]
    testimonials = Testimonial.objects.filter(featured=True).order_by('order')[:6]
    
    # Filtrer les slider items qui ont des images valides
    valid_slider_items = []
    for item in slider_items:
        try:
            if item.image and item.image.url:
                valid_slider_items.append(item)
        except (ValueError, AttributeError):
            pass
    
    # Filtrer les certifications - inclure toutes même sans images
    valid_certifications = list(certifications)
    
    # Filtrer les témoignages qui ont des avatars valides
    valid_testimonials = []
    for testimonial in testimonials:
        try:
            # Toujours inclure, même sans avatar
            valid_testimonials.append(testimonial)
        except (ValueError, AttributeError):
            valid_testimonials.append(testimonial)
    
    context = {
        'slider_items': valid_slider_items,
        'qhse_services': qhse_services,
        'info_services': info_services,
        'qhse_category': qhse_category,
        'info_category': info_category,
        'certifications': valid_certifications,
        'testimonials': valid_testimonials,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """
    Page À propos avec membres de l'équipe
    """
    team_members = TeamMember.objects.all().order_by('order')
    context = {
        'team_members': team_members,
    }
    return render(request, 'core/about.html', context)


@require_http_methods(["GET", "POST"])
def handler404(request, exception):
    """Gestion de l'erreur 404"""
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """Gestion de l'erreur 500"""
    return render(request, 'errors/500.html', status=500)


def handler403(request, exception):
    """Gestion de l'erreur 403"""
    return render(request, 'errors/403.html', status=403)


def contact(request):
    """
    Page contact avec formulaire
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        company = request.POST.get('company', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Validation
        if not all([name, email, subject, message]):
            messages.error(request, 'Veuillez remplir tous les champs obligatoires.')
            return render(request, 'core/contact.html')
        
        # Sauvegarder le message
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,
            subject=subject,
            message=message
        )
        
        # Envoyer un email
        try:
            send_mail(
                subject=f'[Uranus Group] Nouveau message: {subject}',
                message=f'''
Nouveau message de contact:

Nom: {name}
Email: {email}
Téléphone: {phone}
Entreprise: {company}

Message:
{message}
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            # Email de confirmation au client
            send_mail(
                subject='[Uranus Group] Confirmation de réception de votre message',
                message=f'''
Bonjour {name},

Nous avons bien reçu votre message concernant "{subject}".

Notre équipe vous répondra dans les plus brefs délais.

Cordialement,
L'équipe Uranus Group
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            # En cas d'erreur d'email, on continue quand même
            pass
        
        messages.success(request, 'Votre message a été envoyé avec succès. Nous vous répondrons bientôt.')
        return redirect('core:contact')
    
    return render(request, 'core/contact.html')
