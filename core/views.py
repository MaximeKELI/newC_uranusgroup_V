"""
Vues pour l'app core (home, contact, à propos)
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
import google.generativeai as genai
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


@require_http_methods(["POST"])
def chatbot(request):
    """
    Endpoint pour le chatbot IA Gemini
    """
    import logging
    logger = logging.getLogger(__name__)
    
    try:
        # Parser le JSON
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            logger.error(f"Erreur parsing JSON: {e}")
            return JsonResponse({
                'error': 'Format de requête invalide',
                'status': 'error'
            }, status=400)
        
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'error': 'Le message ne peut pas être vide'}, status=400)
        
        # Vérifier que la clé API est configurée
        if not settings.GEMINI_API_KEY:
            logger.error("GEMINI_API_KEY n'est pas configurée")
            return JsonResponse({
                'error': 'Configuration API manquante',
                'status': 'error'
            }, status=500)
        
        # Configuration de l'API Gemini
        try:
            genai.configure(api_key=settings.GEMINI_API_KEY)
        except Exception as e:
            logger.error(f"Erreur configuration Gemini: {e}")
            return JsonResponse({
                'error': f'Erreur de configuration API: {str(e)}',
                'status': 'error'
            }, status=500)
        
        # Créer le modèle
        try:
            model = genai.GenerativeModel('gemini-pro')
        except Exception as e:
            logger.error(f"Erreur création modèle: {e}")
            return JsonResponse({
                'error': f'Erreur création modèle: {str(e)}',
                'status': 'error'
            }, status=500)
        
        # Prompt système pour contextualiser le chatbot
        system_prompt = """Tu es un assistant virtuel pour Uranus Group, une entreprise spécialisée en QHSE (Qualité, Hygiène, Sécurité, Environnement) et Informatique.

Tu dois :
- Répondre de manière professionnelle et amicale
- Fournir des informations sur les services QHSE et Informatique
- Aider les clients à comprendre les certifications ISO
- Orienter les clients vers les services appropriés
- Répondre en français
- Être concis mais informatif

Si tu ne connais pas la réponse, oriente l'utilisateur vers le formulaire de contact ou la page des services."""
        
        # Construire le message complet
        full_message = f"{system_prompt}\n\nUtilisateur: {user_message}\nAssistant:"
        
        # Générer la réponse
        try:
            response = model.generate_content(full_message)
        except Exception as e:
            logger.error(f"Erreur génération contenu Gemini: {e}")
            return JsonResponse({
                'error': f'Erreur API Gemini: {str(e)}',
                'status': 'error'
            }, status=500)
        
        # Extraire le texte de la réponse
        try:
            bot_response = response.text.strip()
        except AttributeError:
            # Si response.text n'existe pas, essayer d'autres méthodes
            try:
                bot_response = str(response).strip()
            except Exception as e:
                logger.error(f"Erreur extraction réponse: {e}, type: {type(response)}")
                return JsonResponse({
                    'error': 'Format de réponse inattendu de l\'API',
                    'status': 'error'
                }, status=500)
        
        return JsonResponse({
            'response': bot_response,
            'status': 'success'
        })
        
    except Exception as e:
        logger.exception(f"Erreur inattendue dans chatbot: {e}")
        return JsonResponse({
            'error': f'Erreur serveur: {str(e)}',
            'status': 'error'
        }, status=500)
