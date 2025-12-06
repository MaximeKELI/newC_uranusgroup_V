"""
Vues pour le dashboard admin personnalisé - Gestion complète de tous les modèles
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator
import json
from datetime import timedelta

# Imports des modèles
from accounts.models import User, UserProfile
from services.models import (
    Service, ServiceRequest, ServiceCategory, 
    Deliverable, Certification, Testimonial
)
from blog.models import Article, Category
from core.models import ContactMessage, TeamMember, SliderItem
from dashboard.models import Notification, SupportTicket, TicketMessage
from dashboard.utils import generate_request_pdf


def admin_required(view_func):
    """Décorateur pour vérifier que l'utilisateur est admin"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin():
            messages.error(request, 'Accès refusé. Vous devez être administrateur.')
            return redirect('core:home')
        return view_func(request, *args, **kwargs)
    return wrapper


# ==================== DASHBOARD PRINCIPAL ====================

@login_required
@admin_required
def admin_dashboard(request):
    """Dashboard admin principal avec statistiques"""
    total_users = User.objects.count()
    total_services = Service.objects.count()
    total_requests = ServiceRequest.objects.count()
    total_articles = Article.objects.count()
    total_categories = ServiceCategory.objects.count()
    total_certifications = Certification.objects.count()
    total_testimonials = Testimonial.objects.count()
    
    requests_by_status = list(ServiceRequest.objects.values('status').annotate(count=Count('id')))
    users_by_role = list(User.objects.values('role').annotate(count=Count('id')))
    recent_requests = ServiceRequest.objects.all().order_by('-created_at')[:10]
    unread_messages = ContactMessage.objects.filter(status='new').count()
    open_tickets = SupportTicket.objects.filter(status__in=['open', 'in_progress']).count()
    
    context = {
        'total_users': total_users,
        'total_services': total_services,
        'total_requests': total_requests,
        'total_articles': total_articles,
        'total_categories': total_categories,
        'total_certifications': total_certifications,
        'total_testimonials': total_testimonials,
        'requests_by_status': mark_safe(json.dumps(list(requests_by_status))),
        'users_by_role': mark_safe(json.dumps(list(users_by_role))),
        'recent_requests': recent_requests,
        'unread_messages': unread_messages,
        'open_tickets': open_tickets,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)


# ==================== GESTION UTILISATEURS ====================

@login_required
@admin_required
def manage_users(request):
    """Liste des utilisateurs"""
    users = User.objects.all().order_by('-created_at')
    role_filter = request.GET.get('role', '')
    search = request.GET.get('search', '')
    
    if role_filter:
        users = users.filter(role=role_filter)
    if search:
        users = users.filter(
            Q(username__icontains=search) |
            Q(email__icontains=search) |
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search)
        )
    
    paginator = Paginator(users, 20)
    page = request.GET.get('page', 1)
    users_page = paginator.get_page(page)
    
    context = {
        'users': users_page,
        'role_filter': role_filter,
        'search': search,
    }
    return render(request, 'dashboard/manage_users.html', context)


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def user_create(request):
    """Créer un utilisateur"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', 'client')
        phone = request.POST.get('phone', '')
        company = request.POST.get('company', '')
        position = request.POST.get('position', '')
        is_active = request.POST.get('is_active') == 'on'
        is_verified = request.POST.get('is_verified') == 'on'
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur existe déjà.')
            return render(request, 'dashboard/user_form.html', {'action': 'create'})
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
            phone=phone,
            company=company,
            position=position,
            is_active=is_active,
            is_verified=is_verified
        )
        
        UserProfile.objects.get_or_create(user=user)
        messages.success(request, f'Utilisateur {username} créé avec succès.')
        return redirect('dashboard:manage_users')
    
    return render(request, 'dashboard/user_form.html', {'action': 'create'})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def user_edit(request, user_id):
    """Modifier un utilisateur"""
    user = get_object_or_404(User, id=user_id)
    profile, _ = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.role = request.POST.get('role', 'client')
        user.phone = request.POST.get('phone', '')
        user.company = request.POST.get('company', '')
        user.position = request.POST.get('position', '')
        user.is_active = request.POST.get('is_active') == 'on'
        user.is_verified = request.POST.get('is_verified') == 'on'
        
        if 'avatar' in request.FILES:
            user.avatar = request.FILES['avatar']
        
        password = request.POST.get('password')
        if password:
            user.set_password(password)
        
        user.save()
        
        profile.bio = request.POST.get('bio', '')
        profile.linkedin = request.POST.get('linkedin', '')
        profile.website = request.POST.get('website', '')
        profile.save()
        
        messages.success(request, f'Utilisateur {user.username} modifié avec succès.')
        return redirect('dashboard:manage_users')
    
    context = {
        'user': user,
        'profile': profile,
        'action': 'edit',
    }
    return render(request, 'dashboard/user_form.html', context)


@login_required
@admin_required
@require_http_methods(["POST"])
def user_delete(request, user_id):
    """Supprimer un utilisateur"""
    user = get_object_or_404(User, id=user_id)
    if user == request.user:
        messages.error(request, 'Vous ne pouvez pas supprimer votre propre compte.')
    else:
        username = user.username
        user.delete()
        messages.success(request, f'Utilisateur {username} supprimé avec succès.')
    return redirect('dashboard:manage_users')


# ==================== GESTION SERVICES ====================

@login_required
@admin_required
def manage_services(request):
    """Liste des services"""
    services = Service.objects.all().order_by('category', 'order')
    category_filter = request.GET.get('category', '')
    search = request.GET.get('search', '')
    
    if category_filter:
        services = services.filter(category_id=category_filter)
    if search:
        services = services.filter(
            Q(name__icontains=search) |
            Q(short_description__icontains=search)
        )
    
    categories = ServiceCategory.objects.all()
    paginator = Paginator(services, 20)
    page = request.GET.get('page', 1)
    services_page = paginator.get_page(page)
    
    context = {
        'services': services_page,
        'categories': categories,
        'category_filter': category_filter,
        'search': search,
    }
    return render(request, 'dashboard/manage_services.html', context)


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def service_create(request):
    """Créer un service"""
    if request.method == 'POST':
        service = Service.objects.create(
            category_id=request.POST.get('category'),
            name=request.POST.get('name'),
            slug=request.POST.get('slug'),
            short_description=request.POST.get('short_description'),
            full_description=request.POST.get('full_description'),
            icon=request.POST.get('icon', ''),
            price_starting_from=request.POST.get('price_starting_from') or None,
            duration=request.POST.get('duration', ''),
            status=request.POST.get('status', 'active'),
            featured=request.POST.get('featured') == 'on',
            order=int(request.POST.get('order', 0)),
        )
        
        if 'image' in request.FILES:
            service.image = request.FILES['image']
            service.save()
        
        messages.success(request, f'Service {service.name} créé avec succès.')
        return redirect('dashboard:manage_services')
    
    categories = ServiceCategory.objects.all()
    return render(request, 'dashboard/service_form.html', {
        'action': 'create',
        'categories': categories,
    })


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def service_edit(request, service_id):
    """Modifier un service"""
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        service.category_id = request.POST.get('category')
        service.name = request.POST.get('name')
        service.slug = request.POST.get('slug')
        service.short_description = request.POST.get('short_description')
        service.full_description = request.POST.get('full_description')
        service.icon = request.POST.get('icon', '')
        service.price_starting_from = request.POST.get('price_starting_from') or None
        service.duration = request.POST.get('duration', '')
        service.status = request.POST.get('status', 'active')
        service.featured = request.POST.get('featured') == 'on'
        service.order = int(request.POST.get('order', 0))
        
        if 'image' in request.FILES:
            service.image = request.FILES['image']
        
        service.save()
        messages.success(request, f'Service {service.name} modifié avec succès.')
        return redirect('dashboard:manage_services')
    
    categories = ServiceCategory.objects.all()
    return render(request, 'dashboard/service_form.html', {
        'service': service,
        'action': 'edit',
        'categories': categories,
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def service_delete(request, service_id):
    """Supprimer un service"""
    service = get_object_or_404(Service, id=service_id)
    name = service.name
    service.delete()
    messages.success(request, f'Service {name} supprimé avec succès.')
    return redirect('dashboard:manage_services')


# ==================== GESTION CATÉGORIES DE SERVICES ====================

@login_required
@admin_required
def manage_service_categories(request):
    """Liste des catégories de services"""
    categories = ServiceCategory.objects.all().order_by('order')
    return render(request, 'dashboard/manage_service_categories.html', {'categories': categories})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def service_category_create(request):
    """Créer une catégorie de service"""
    if request.method == 'POST':
        category = ServiceCategory.objects.create(
            name=request.POST.get('name'),
            slug=request.POST.get('slug'),
            description=request.POST.get('description', ''),
            icon=request.POST.get('icon', ''),
            color=request.POST.get('color', '#0DE1E7'),
            order=int(request.POST.get('order', 0)),
        )
        messages.success(request, f'Catégorie {category.name} créée avec succès.')
        return redirect('dashboard:manage_service_categories')
    
    return render(request, 'dashboard/service_category_form.html', {'action': 'create'})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def service_category_edit(request, category_id):
    """Modifier une catégorie de service"""
    category = get_object_or_404(ServiceCategory, id=category_id)
    
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.slug = request.POST.get('slug')
        category.description = request.POST.get('description', '')
        category.icon = request.POST.get('icon', '')
        category.color = request.POST.get('color', '#0DE1E7')
        category.order = int(request.POST.get('order', 0))
        category.save()
        
        messages.success(request, f'Catégorie {category.name} modifiée avec succès.')
        return redirect('dashboard:manage_service_categories')
    
    return render(request, 'dashboard/service_category_form.html', {
        'category': category,
        'action': 'edit',
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def service_category_delete(request, category_id):
    """Supprimer une catégorie de service"""
    category = get_object_or_404(ServiceCategory, id=category_id)
    name = category.name
    category.delete()
    messages.success(request, f'Catégorie {name} supprimée avec succès.')
    return redirect('dashboard:manage_service_categories')


# ==================== GESTION DEMANDES DE SERVICE ====================

@login_required
@admin_required
def manage_requests(request):
    """Liste des demandes de service"""
    requests = ServiceRequest.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status', '')
    search = request.GET.get('search', '')
    
    if status_filter:
        requests = requests.filter(status=status_filter)
    if search:
        requests = requests.filter(
            Q(title__icontains=search) |
            Q(client__username__icontains=search) |
            Q(service__name__icontains=search)
        )
    
    paginator = Paginator(requests, 20)
    page = request.GET.get('page', 1)
    requests_page = paginator.get_page(page)
    
    context = {
        'requests': requests_page,
        'status_filter': status_filter,
        'search': search,
    }
    return render(request, 'dashboard/manage_requests.html', context)


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def request_edit(request, request_id):
    """Modifier une demande de service"""
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    
    if request.method == 'POST':
        service_request.title = request.POST.get('title')
        service_request.description = request.POST.get('description')
        service_request.status = request.POST.get('status')
        service_request.priority = request.POST.get('priority')
        service_request.assigned_to_id = request.POST.get('assigned_to') or None
        
        deadline = request.POST.get('deadline')
        if deadline:
            service_request.deadline = deadline
        
        if service_request.status == 'completed' and not service_request.completed_at:
            service_request.completed_at = timezone.now()
        
        service_request.save()
        messages.success(request, 'Demande modifiée avec succès.')
        return redirect('dashboard:manage_requests')
    
    users = User.objects.filter(
        Q(role='admin') | Q(role='manager_qhse') | Q(role='manager_info')
    )
    deliverables = Deliverable.objects.filter(request=service_request)
    
    return render(request, 'dashboard/request_form.html', {
        'service_request': service_request,
        'users': users,
        'deliverables': deliverables,
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def request_delete(request, request_id):
    """Supprimer une demande de service"""
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    title = service_request.title
    service_request.delete()
    messages.success(request, f'Demande {title} supprimée avec succès.')
    return redirect('dashboard:manage_requests')


@login_required
@admin_required
def request_export_pdf(request, request_id):
    """Exporter une demande en PDF"""
    pdf_response = generate_request_pdf(request_id)
    if pdf_response:
        return pdf_response
    messages.error(request, 'Erreur lors de la génération du PDF.')
    return redirect('dashboard:manage_requests')


# ==================== GESTION CERTIFICATIONS ====================

@login_required
@admin_required
def manage_certifications(request):
    """Liste des certifications"""
    certifications = Certification.objects.all().order_by('order')
    return render(request, 'dashboard/manage_certifications.html', {'certifications': certifications})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def certification_create(request):
    """Créer une certification"""
    if request.method == 'POST':
        certification = Certification.objects.create(
            name=request.POST.get('name'),
            code=request.POST.get('code'),
            description=request.POST.get('description', ''),
            category_id=request.POST.get('category'),
            order=int(request.POST.get('order', 0)),
        )
        
        if 'image' in request.FILES:
            certification.image = request.FILES['image']
            certification.save()
        
        messages.success(request, f'Certification {certification.name} créée avec succès.')
        return redirect('dashboard:manage_certifications')
    
    categories = ServiceCategory.objects.all()
    return render(request, 'dashboard/certification_form.html', {
        'action': 'create',
        'categories': categories,
    })


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def certification_edit(request, cert_id):
    """Modifier une certification"""
    certification = get_object_or_404(Certification, id=cert_id)
    
    if request.method == 'POST':
        certification.name = request.POST.get('name')
        certification.code = request.POST.get('code')
        certification.description = request.POST.get('description', '')
        certification.category_id = request.POST.get('category')
        certification.order = int(request.POST.get('order', 0))
        
        if 'image' in request.FILES:
            certification.image = request.FILES['image']
        
        certification.save()
        messages.success(request, f'Certification {certification.name} modifiée avec succès.')
        return redirect('dashboard:manage_certifications')
    
    categories = ServiceCategory.objects.all()
    return render(request, 'dashboard/certification_form.html', {
        'certification': certification,
        'action': 'edit',
        'categories': categories,
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def certification_delete(request, cert_id):
    """Supprimer une certification"""
    certification = get_object_or_404(Certification, id=cert_id)
    name = certification.name
    certification.delete()
    messages.success(request, f'Certification {name} supprimée avec succès.')
    return redirect('dashboard:manage_certifications')


# ==================== GESTION TÉMOIGNAGES ====================

@login_required
@admin_required
def manage_testimonials(request):
    """Liste des témoignages"""
    testimonials = Testimonial.objects.all().order_by('order', '-created_at')
    return render(request, 'dashboard/manage_testimonials.html', {'testimonials': testimonials})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def testimonial_create(request):
    """Créer un témoignage"""
    if request.method == 'POST':
        testimonial = Testimonial.objects.create(
            client_name=request.POST.get('client_name'),
            client_position=request.POST.get('client_position', ''),
            client_company=request.POST.get('client_company', ''),
            content=request.POST.get('content'),
            rating=int(request.POST.get('rating', 5)),
            service_id=request.POST.get('service') or None,
            featured=request.POST.get('featured') == 'on',
            order=int(request.POST.get('order', 0)),
        )
        
        if 'client_avatar' in request.FILES:
            testimonial.client_avatar = request.FILES['client_avatar']
            testimonial.save()
        
        messages.success(request, f'Témoignage de {testimonial.client_name} créé avec succès.')
        return redirect('dashboard:manage_testimonials')
    
    services = Service.objects.all()
    return render(request, 'dashboard/testimonial_form.html', {
        'action': 'create',
        'services': services,
    })


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def testimonial_edit(request, testimonial_id):
    """Modifier un témoignage"""
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    
    if request.method == 'POST':
        testimonial.client_name = request.POST.get('client_name')
        testimonial.client_position = request.POST.get('client_position', '')
        testimonial.client_company = request.POST.get('client_company', '')
        testimonial.content = request.POST.get('content')
        testimonial.rating = int(request.POST.get('rating', 5))
        testimonial.service_id = request.POST.get('service') or None
        testimonial.featured = request.POST.get('featured') == 'on'
        testimonial.order = int(request.POST.get('order', 0))
        
        if 'client_avatar' in request.FILES:
            testimonial.client_avatar = request.FILES['client_avatar']
        
        testimonial.save()
        messages.success(request, f'Témoignage de {testimonial.client_name} modifié avec succès.')
        return redirect('dashboard:manage_testimonials')
    
    services = Service.objects.all()
    return render(request, 'dashboard/testimonial_form.html', {
        'testimonial': testimonial,
        'action': 'edit',
        'services': services,
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def testimonial_delete(request, testimonial_id):
    """Supprimer un témoignage"""
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    name = testimonial.client_name
    testimonial.delete()
    messages.success(request, f'Témoignage de {name} supprimé avec succès.')
    return redirect('dashboard:manage_testimonials')


# ==================== GESTION ARTICLES ====================

@login_required
@admin_required
def manage_articles(request):
    """Liste des articles"""
    articles = Article.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status', '')
    search = request.GET.get('search', '')
    
    if status_filter:
        articles = articles.filter(status=status_filter)
    if search:
        articles = articles.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        )
    
    paginator = Paginator(articles, 20)
    page = request.GET.get('page', 1)
    articles_page = paginator.get_page(page)
    
    context = {
        'articles': articles_page,
        'status_filter': status_filter,
        'search': search,
    }
    return render(request, 'dashboard/manage_articles.html', context)


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def article_create(request):
    """Créer un article"""
    if request.method == 'POST':
        article = Article.objects.create(
            title=request.POST.get('title'),
            slug=request.POST.get('slug'),
            author=request.user,
            category_id=request.POST.get('category') or None,
            excerpt=request.POST.get('excerpt', ''),
            content=request.POST.get('content'),
            status=request.POST.get('status', 'draft'),
            featured=request.POST.get('featured') == 'on',
        )
        
        if 'featured_image' in request.FILES:
            article.featured_image = request.FILES['featured_image']
            article.save()
        
        messages.success(request, f'Article {article.title} créé avec succès.')
        return redirect('dashboard:manage_articles')
    
    categories = Category.objects.all()
    return render(request, 'dashboard/article_form.html', {
        'action': 'create',
        'categories': categories,
    })


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def article_edit(request, article_id):
    """Modifier un article"""
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.slug = request.POST.get('slug')
        article.category_id = request.POST.get('category') or None
        article.excerpt = request.POST.get('excerpt', '')
        article.content = request.POST.get('content')
        article.status = request.POST.get('status', 'draft')
        article.featured = request.POST.get('featured') == 'on'
        
        if 'featured_image' in request.FILES:
            article.featured_image = request.FILES['featured_image']
        
        article.save()
        messages.success(request, f'Article {article.title} modifié avec succès.')
        return redirect('dashboard:manage_articles')
    
    categories = Category.objects.all()
    return render(request, 'dashboard/article_form.html', {
        'article': article,
        'action': 'edit',
        'categories': categories,
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def article_delete(request, article_id):
    """Supprimer un article"""
    article = get_object_or_404(Article, id=article_id)
    title = article.title
    article.delete()
    messages.success(request, f'Article {title} supprimé avec succès.')
    return redirect('dashboard:manage_articles')


# ==================== GESTION CATÉGORIES DE BLOG ====================

@login_required
@admin_required
def manage_blog_categories(request):
    """Liste des catégories de blog"""
    categories = Category.objects.all().order_by('order')
    return render(request, 'dashboard/manage_blog_categories.html', {'categories': categories})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def blog_category_create(request):
    """Créer une catégorie de blog"""
    if request.method == 'POST':
        category = Category.objects.create(
            name=request.POST.get('name'),
            slug=request.POST.get('slug'),
            description=request.POST.get('description', ''),
            color=request.POST.get('color', '#0DE1E7'),
            order=int(request.POST.get('order', 0)),
        )
        messages.success(request, f'Catégorie {category.name} créée avec succès.')
        return redirect('dashboard:manage_blog_categories')
    
    return render(request, 'dashboard/blog_category_form.html', {'action': 'create'})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def blog_category_edit(request, category_id):
    """Modifier une catégorie de blog"""
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.slug = request.POST.get('slug')
        category.description = request.POST.get('description', '')
        category.color = request.POST.get('color', '#0DE1E7')
        category.order = int(request.POST.get('order', 0))
        category.save()
        
        messages.success(request, f'Catégorie {category.name} modifiée avec succès.')
        return redirect('dashboard:manage_blog_categories')
    
    return render(request, 'dashboard/blog_category_form.html', {
        'category': category,
        'action': 'edit',
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def blog_category_delete(request, category_id):
    """Supprimer une catégorie de blog"""
    category = get_object_or_404(Category, id=category_id)
    name = category.name
    category.delete()
    messages.success(request, f'Catégorie {name} supprimée avec succès.')
    return redirect('dashboard:manage_blog_categories')


# ==================== GESTION SLIDER ====================

@login_required
@admin_required
def manage_slider(request):
    """Liste des items du slider"""
    items = SliderItem.objects.all().order_by('order')
    return render(request, 'dashboard/manage_slider.html', {'items': items})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def slider_item_create(request):
    """Créer un item de slider"""
    if request.method == 'POST':
        item = SliderItem.objects.create(
            title=request.POST.get('title'),
            subtitle=request.POST.get('subtitle', ''),
            description=request.POST.get('description', ''),
            button_text=request.POST.get('button_text', ''),
            button_link=request.POST.get('button_link', ''),
            active=request.POST.get('active') == 'on',
            order=int(request.POST.get('order', 0)),
        )
        
        if 'image' in request.FILES:
            item.image = request.FILES['image']
            item.save()
        
        messages.success(request, f'Item de slider {item.title} créé avec succès.')
        return redirect('dashboard:manage_slider')
    
    return render(request, 'dashboard/slider_item_form.html', {'action': 'create'})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def slider_item_edit(request, item_id):
    """Modifier un item de slider"""
    item = get_object_or_404(SliderItem, id=item_id)
    
    if request.method == 'POST':
        item.title = request.POST.get('title')
        item.subtitle = request.POST.get('subtitle', '')
        item.description = request.POST.get('description', '')
        item.button_text = request.POST.get('button_text', '')
        item.button_link = request.POST.get('button_link', '')
        item.active = request.POST.get('active') == 'on'
        item.order = int(request.POST.get('order', 0))
        
        if 'image' in request.FILES:
            item.image = request.FILES['image']
        
        item.save()
        messages.success(request, f'Item de slider {item.title} modifié avec succès.')
        return redirect('dashboard:manage_slider')
    
    return render(request, 'dashboard/slider_item_form.html', {
        'item': item,
        'action': 'edit',
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def slider_item_delete(request, item_id):
    """Supprimer un item de slider"""
    item = get_object_or_404(SliderItem, id=item_id)
    title = item.title
    item.delete()
    messages.success(request, f'Item de slider {title} supprimé avec succès.')
    return redirect('dashboard:manage_slider')


# ==================== GESTION ÉQUIPE ====================

@login_required
@admin_required
def manage_team(request):
    """Liste des membres de l'équipe"""
    members = TeamMember.objects.all().order_by('order')
    return render(request, 'dashboard/manage_team.html', {'members': members})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def team_member_create(request):
    """Créer un membre de l'équipe"""
    if request.method == 'POST':
        member = TeamMember.objects.create(
            name=request.POST.get('name'),
            position=request.POST.get('position'),
            bio=request.POST.get('bio', ''),
            email=request.POST.get('email', ''),
            linkedin=request.POST.get('linkedin', ''),
            order=int(request.POST.get('order', 0)),
        )
        
        if 'photo' in request.FILES:
            member.photo = request.FILES['photo']
            member.save()
        
        messages.success(request, f'Membre {member.name} créé avec succès.')
        return redirect('dashboard:manage_team')
    
    return render(request, 'dashboard/team_member_form.html', {'action': 'create'})


@login_required
@admin_required
@require_http_methods(["GET", "POST"])
def team_member_edit(request, member_id):
    """Modifier un membre de l'équipe"""
    member = get_object_or_404(TeamMember, id=member_id)
    
    if request.method == 'POST':
        member.name = request.POST.get('name')
        member.position = request.POST.get('position')
        member.bio = request.POST.get('bio', '')
        member.email = request.POST.get('email', '')
        member.linkedin = request.POST.get('linkedin', '')
        member.order = int(request.POST.get('order', 0))
        
        if 'photo' in request.FILES:
            member.photo = request.FILES['photo']
        
        member.save()
        messages.success(request, f'Membre {member.name} modifié avec succès.')
        return redirect('dashboard:manage_team')
    
    return render(request, 'dashboard/team_member_form.html', {
        'member': member,
        'action': 'edit',
    })


@login_required
@admin_required
@require_http_methods(["POST"])
def team_member_delete(request, member_id):
    """Supprimer un membre de l'équipe"""
    member = get_object_or_404(TeamMember, id=member_id)
    name = member.name
    member.delete()
    messages.success(request, f'Membre {name} supprimé avec succès.')
    return redirect('dashboard:manage_team')


# ==================== GESTION MESSAGES DE CONTACT ====================

@login_required
@admin_required
def manage_contact_messages(request):
    """Liste des messages de contact"""
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status', '')
    
    if status_filter:
        messages_list = messages_list.filter(status=status_filter)
    
    paginator = Paginator(messages_list, 20)
    page = request.GET.get('page', 1)
    messages_page = paginator.get_page(page)
    
    context = {
        'messages': messages_page,
        'status_filter': status_filter,
    }
    return render(request, 'dashboard/manage_contact_messages.html', context)


@login_required
@admin_required
@require_http_methods(["POST"])
def contact_message_update_status(request, message_id):
    """Mettre à jour le statut d'un message"""
    message = get_object_or_404(ContactMessage, id=message_id)
    message.status = request.POST.get('status')
    if message.status == 'replied':
        message.replied_at = timezone.now()
    message.save()
    messages.success(request, 'Statut du message mis à jour.')
    return redirect('dashboard:manage_contact_messages')


@login_required
@admin_required
@require_http_methods(["POST"])
def contact_message_delete(request, message_id):
    """Supprimer un message de contact"""
    message = get_object_or_404(ContactMessage, id=message_id)
    subject = message.subject
    message.delete()
    messages.success(request, f'Message {subject} supprimé avec succès.')
    return redirect('dashboard:manage_contact_messages')


# ==================== GESTION TICKETS ====================

@login_required
@admin_required
def manage_tickets(request):
    """Liste des tickets de support"""
    tickets = SupportTicket.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status', '')
    
    if status_filter:
        tickets = tickets.filter(status=status_filter)
    
    paginator = Paginator(tickets, 20)
    page = request.GET.get('page', 1)
    tickets_page = paginator.get_page(page)
    
    context = {
        'tickets': tickets_page,
        'status_filter': status_filter,
    }
    return render(request, 'dashboard/manage_tickets.html', context)


@login_required
def ticket_detail(request, ticket_id):
    """Détail d'un ticket de support"""
    ticket = get_object_or_404(SupportTicket, id=ticket_id)
    
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
@admin_required
@require_http_methods(["POST"])
def ticket_update_status(request, ticket_id):
    """Mettre à jour le statut d'un ticket"""
    ticket = get_object_or_404(SupportTicket, id=ticket_id)
    ticket.status = request.POST.get('status')
    ticket.assigned_to_id = request.POST.get('assigned_to') or None
    
    if ticket.status == 'resolved':
        ticket.resolved_at = timezone.now()
    
    ticket.save()
    messages.success(request, 'Statut du ticket mis à jour.')
    return redirect('dashboard:manage_tickets')


@login_required
@require_http_methods(["POST"])
def create_ticket(request):
    """Créer un nouveau ticket de support"""
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


# ==================== NOTIFICATIONS ====================

@login_required
def notifications(request):
    """Liste des notifications de l'utilisateur"""
    notifications_list = Notification.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'notifications': notifications_list,
    }
    return render(request, 'dashboard/notifications.html', context)


@login_required
@require_http_methods(["POST"])
def mark_notification_read(request, notification_id):
    """Marquer une notification comme lue"""
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.read = True
    notification.save()
    return JsonResponse({'success': True})


@login_required
@require_http_methods(["POST"])
def mark_all_notifications_read(request):
    """Marquer toutes les notifications comme lues"""
    Notification.objects.filter(user=request.user, read=False).update(read=True)
    return JsonResponse({'success': True})
