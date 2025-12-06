"""
Vues pour les services QHSE et Informatique
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Service, ServiceCategory, ServiceRequest, Deliverable


def service_list(request):
    """
    Liste de tous les services
    """
    category_slug = request.GET.get('category')
    search = request.GET.get('search', '')
    
    services = Service.objects.filter(status='active')
    
    if category_slug:
        category = get_object_or_404(ServiceCategory, slug=category_slug)
        services = services.filter(category=category)
    
    if search:
        services = services.filter(
            Q(name__icontains=search) |
            Q(short_description__icontains=search) |
            Q(full_description__icontains=search)
        )
    
    categories = ServiceCategory.objects.all()
    
    context = {
        'services': services,
        'categories': categories,
        'current_category': category_slug,
        'search': search,
    }
    return render(request, 'services/service_list.html', context)


def service_detail(request, slug):
    """
    Détail d'un service
    """
    service = get_object_or_404(Service, slug=slug, status='active')
    related_services = Service.objects.filter(
        category=service.category,
        status='active'
    ).exclude(id=service.id)[:4]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/service_detail.html', context)


@login_required
def request_service(request, service_id):
    """
    Créer une demande de service
    """
    service = get_object_or_404(Service, id=service_id, status='active')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority', 'medium')
        deadline = request.POST.get('deadline') or None
        
        if title and description:
            service_request = ServiceRequest.objects.create(
                service=service,
                client=request.user,
                title=title,
                description=description,
                priority=priority,
                deadline=deadline
            )
            
            # Créer une notification pour les managers
            from dashboard.models import Notification
            managers = request.user.__class__.objects.filter(
                Q(role='manager_qhse') | Q(role='manager_info') | Q(role='admin')
            )
            for manager in managers:
                Notification.objects.create(
                    user=manager,
                    title=f'Nouvelle demande de service',
                    message=f'{request.user.username} a créé une demande pour "{service.name}"',
                    type='info'
                )
            
            from django.contrib import messages
            messages.success(request, 'Votre demande de service a été créée avec succès.')
            return redirect('accounts:dashboard')
    
    context = {
        'service': service,
    }
    return render(request, 'services/request_service.html', context)


@login_required
def my_requests(request):
    """
    Liste des demandes de service de l'utilisateur
    """
    requests = ServiceRequest.objects.filter(client=request.user).order_by('-created_at')
    
    context = {
        'requests': requests,
    }
    return render(request, 'services/my_requests.html', context)


@login_required
def request_detail(request, request_id):
    """
    Détail d'une demande de service
    """
    service_request = get_object_or_404(
        ServiceRequest,
        id=request_id,
        client=request.user
    )
    deliverables = Deliverable.objects.filter(request=service_request)
    
    context = {
        'service_request': service_request,
        'deliverables': deliverables,
    }
    return render(request, 'services/request_detail.html', context)
