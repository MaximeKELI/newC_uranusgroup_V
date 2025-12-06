"""
Script pour créer un superutilisateur automatiquement
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uranusgroup.settings')
django.setup()

from accounts.models import User

def create_superuser():
    """Créer un superutilisateur par défaut"""
    username = 'admin'
    email = 'admin@uranusgroup.com'
    password = 'admin123'  # À changer en production !
    
    if User.objects.filter(username=username).exists():
        print(f"L'utilisateur '{username}' existe déjà.")
        return
    
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password,
        role='admin',
        is_verified=True
    )
    
    print(f"Superutilisateur créé avec succès !")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print("\n⚠️  ATTENTION: Changez le mot de passe en production !")

if __name__ == '__main__':
    create_superuser()

