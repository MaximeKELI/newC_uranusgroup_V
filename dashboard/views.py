"""
Vues pour le dashboard admin personnalisé
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.utils.safestring import mark_safe
import json
from datetime import timedelta
from accounts.models import User
from services.models import Service, ServiceRequest, ServiceCategory
from blog.models import Article, Category
from core.models import ContactMessage
from .models import Notification, SupportTicket, TicketMessage


def admin_required(view_func):
    """
    Décorateur pour vérifier que l'utilisateur est admin
    """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin():
            messages.error(request, 'Accès refusé. Vous devez être administrateur.')
            return redirect('core:home')
        return view_func(request, *args, **kwargs)
    return wrapper


@login_required
@admin_required
def admin_dashboard(request):
    """
    Dashboard admin principal avec statistiques
    """
    # Statistiques générales
    total_users = User.objects.count()
    total_services = Service.objects.count()
    total_requests = ServiceRequest.objects.count()
    total_articles = Article.objects.count()
    
    # Demandes par statut
    requests_by_status = list(ServiceRequest.objects.values('status').annotate(count=Count('id')))
    
    # Utilisateurs par rôle
    users_by_role = list(User.objects.values('role').annotate(count=Count('id')))
    
    # Demandes récentes
    recent_requests = ServiceRequest.objects.all().order_by('-created_at')[:10]
    
    # Messages de contact non lus
    unread_messages = ContactMessage.objects.filter(status='new').count()
    
    # Tickets ouverts
    open_tickets = SupportTicket.objects.filter(status__in=['open', 'in_progress']).count()
    
    context = {
        'total_users': total_users,
        'total_services': total_services,
        'total_requests': total_requests,
        'total_articles': total_articles,
        'requests_by_status': mark_safe(json.dumps(list(requests_by_status))),
        'users_by_role': mark_safe(json.dumps(list(users_by_role))),
        'recent_requests': recent_requests,
        'unread_messages': unread_messages,
        'open_tickets': open_tickets,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)


@login_required
@admin_required
def manage_users(request):
    """
    Gestion des utilisateurs
    """
    users = User.objects.all().order_by('-created_at')
    role_filter = request.GET.get('role', '')
    
    if role_filter:
        users = users.filter(role=role_filter)
    
    context = {
        'users': users,
        'role_filter': role_filter,
    }
    return render(request, 'dashboard/manage_users.html', context)


@login_required
@admin_required
def manage_services(request):
    """
    Gestion des services
    """
    services = Service.objects.all().order_by('category', 'order')
    categories = ServiceCategory.objects.all()
    
    context = {
        'services': services,
        'categories': categories,
    }
    return render(request, 'dashboard/manage_services.html', context)


@login_required
@admin_required
def manage_requests(request):
    """
    Gestion des demandes de service
    """
    requests = ServiceRequest.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status', '')
    
    if status_filter:
        requests = requests.filter(status=status_filter)
    
    context = {
        'requests': requests,
        'status_filter': status_filter,
    }
    return render(request, 'dashboard/manage_requests.html', context)


@login_required
@admin_required
def manage_articles(request):
    """
    Gestion des articles de blog
    """
    articles = Article.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status', '')
    
    if status_filter:
        articles = articles.filter(status=status_filter)
    
    context = {
        'articles': articles,
        'status_filter': status_filter,
    }
    return render(request, 'dashboard/manage_articles.html', context)


@login_required
@admin_required
def manage_tickets(request):
    """
    Gestion des tickets de support
    """
    tickets = SupportTicket.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status', '')
    
    if status_filter:
        tickets = tickets.filter(status=status_filter)
    
    context = {
        'tickets': tickets,
        'status_filter': status_filter,
    }
    return render(request, 'dashboard/manage_tickets.html', context)


@login_required
def ticket_detail(request, ticket_id):
    """
    Détail d'un ticket de support
    """
    ticket = get_object_or_404(SupportTicket, id=ticket_id)
    
    # Vérifier les permissions
    if not (request.user.is_admin() or ticket.user == request.user or ticket.assigned_to == request.user):
        messages.error(request, 'Accès refusé.')
        return redirect('accounts:dashboard')
    
    messages_list = TicketMessage.objects.filter(ticket=ticket).order_by('created_at')
    
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            TicketMessage.objects.create(
                ticket=ticket,
                user=request.user,
                message=message_text
            )
            
            # Mettre à jour le statut si c'est un admin qui répond
            if request.user.is_admin() and ticket.status == 'open':
                ticket.status = 'in_progress'
                ticket.assigned_to = request.user
                ticket.save()
            
            messages.success(request, 'Message envoyé.')
            return redirect('dashboard:ticket_detail', ticket_id=ticket.id)
    
    context = {
        'ticket': ticket,
        'messages': messages_list,
    }
    return render(request, 'dashboard/ticket_detail.html', context)


@login_required
@require_http_methods(["POST"])
def create_ticket(request):
    """
    Créer un nouveau ticket de support
    """
    subject = request.POST.get('subject')
    description = request.POST.get('description')
    priority = request.POST.get('priority', 'medium')
    
    if subject and description:
        ticket = SupportTicket.objects.create(
            user=request.user,
            subject=subject,
            description=description,
            priority=priority
        )
        
        # Notifier les admins
        admins = User.objects.filter(Q(role='admin') | Q(is_superuser=True))
        for admin in admins:
            Notification.objects.create(
                user=admin,
                title='Nouveau ticket de support',
                message=f'{request.user.username} a créé un ticket: {subject}',
                type='info'
            )
        
        messages.success(request, 'Ticket créé avec succès.')
        return redirect('accounts:dashboard')
    
    messages.error(request, 'Veuillez remplir tous les champs.')
    return redirect('accounts:dashboard')


@login_required
def notifications(request):
    """
    Liste des notifications de l'utilisateur
    """
    notifications_list = Notification.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'notifications': notifications_list,
    }
    return render(request, 'dashboard/notifications.html', context)


@login_required
@require_http_methods(["POST"])
def mark_notification_read(request, notification_id):
    """
    Marquer une notification comme lue
    """
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    return JsonResponse({'success': True})


@login_required
@require_http_methods(["POST"])
def mark_all_notifications_read(request):
    """
    Marquer toutes les notifications comme lues
    """
    Notification.objects.filter(user=request.user, read=False).update(read=True)
    return JsonResponse({'success': True})
