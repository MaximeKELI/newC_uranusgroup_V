"""
Vues pour l'authentification et gestion des comptes
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import User, UserProfile
from services.models import ServiceRequest
from dashboard.models import Notification


@require_http_methods(["GET", "POST"])
def register(request):
    """
    Inscription d'un nouvel utilisateur
    """
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role', 'client')
        phone = request.POST.get('phone', '')
        company = request.POST.get('company', '')
        
        # Validation
        if password1 != password2:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà pris.')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
            return render(request, 'accounts/register.html')
        
        # Créer l'utilisateur
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            role=role,
            phone=phone,
            company=company
        )
        
        # Créer le profil
        UserProfile.objects.create(user=user)
        
        # Connecter l'utilisateur
        login(request, user)
        messages.success(request, 'Inscription réussie ! Bienvenue sur Uranus Group.')
        return redirect('accounts:dashboard')
    
    return render(request, 'accounts/register.html')


@require_http_methods(["GET", "POST"])
def login_view(request):
    """
    Connexion utilisateur
    """
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenue, {user.username} !')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    
    return render(request, 'accounts/login.html')


@login_required
def dashboard(request):
    """
    Tableau de bord utilisateur
    """
    user = request.user
    requests = ServiceRequest.objects.filter(client=user).order_by('-created_at')[:5]
    notifications = Notification.objects.filter(user=user, read=False).order_by('-created_at')[:5]
    
    context = {
        'user': user,
        'requests': requests,
        'notifications': notifications,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def profile(request):
    """
    Profil utilisateur
    """
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.phone = request.POST.get('phone', '')
        user.company = request.POST.get('company', '')
        user.position = request.POST.get('position', '')
        profile.bio = request.POST.get('bio', '')
        profile.linkedin = request.POST.get('linkedin', '')
        profile.website = request.POST.get('website', '')
        
        if 'avatar' in request.FILES:
            user.avatar = request.FILES['avatar']
        
        user.save()
        profile.save()
        
        messages.success(request, 'Profil mis à jour avec succès.')
        return redirect('accounts:profile')
    
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'accounts/profile.html', context)
