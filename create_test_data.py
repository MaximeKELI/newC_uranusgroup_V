"""
Script pour créer des données de test
"""
import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uranusgroup.settings')
django.setup()

from accounts.models import User, UserProfile
from services.models import ServiceCategory, Service, Certification, Testimonial
from blog.models import Category, Article
from core.models import SliderItem, TeamMember

def create_test_data():
    """Créer des données de test pour le site"""
    
    print("Création des données de test...")
    
    # 1. Catégories de services
    print("1. Création des catégories de services...")
    qhse_cat, _ = ServiceCategory.objects.get_or_create(
        slug='qhse',
        defaults={
            'name': 'QHSE',
            'description': 'Qualité, Hygiène, Sécurité, Environnement',
            'icon': 'fas fa-shield-alt',
            'color': '#0DE1E7',
            'order': 1
        }
    )
    
    info_cat, _ = ServiceCategory.objects.get_or_create(
        slug='informatique',
        defaults={
            'name': 'Informatique',
            'description': 'Solutions informatiques et cybersécurité',
            'icon': 'fas fa-laptop-code',
            'color': '#0DE1E7',
            'order': 2
        }
    )
    
    # 2. Services QHSE
    print("2. Création des services QHSE...")
    services_qhse = [
        {
            'name': 'Certification ISO 9001',
            'slug': 'certification-iso-9001',
            'short_description': 'Accompagnement complet pour l\'obtention de la certification ISO 9001 (Qualité)',
            'full_description': '''La certification ISO 9001 est la norme internationale de référence pour les systèmes de management de la qualité. 

Nous vous accompagnons dans :
- L'audit de votre système actuel
- La mise en conformité avec les exigences ISO 9001:2015
- La préparation à la certification
- Le suivi post-certification

Durée moyenne : 6 à 12 mois selon la taille de votre entreprise.''',
            'category': qhse_cat,
            'icon': 'fas fa-certificate',
            'price_starting_from': 5000.00,
            'duration': '6-12 mois',
            'featured': True,
            'order': 1
        },
        {
            'name': 'Certification ISO 14001',
            'slug': 'certification-iso-14001',
            'short_description': 'Mise en place d\'un système de management environnemental conforme ISO 14001',
            'full_description': '''ISO 14001 est la norme pour les systèmes de management environnemental. 

Notre accompagnement comprend :
- Analyse de l'impact environnemental
- Mise en place du système de management
- Formation des équipes
- Préparation à la certification
- Suivi et amélioration continue''',
            'category': qhse_cat,
            'icon': 'fas fa-leaf',
            'price_starting_from': 6000.00,
            'duration': '6-12 mois',
            'featured': True,
            'order': 2
        },
        {
            'name': 'Certification ISO 45001',
            'slug': 'certification-iso-45001',
            'short_description': 'Système de management de la santé et sécurité au travail (SST)',
            'full_description': '''ISO 45001 remplace OHSAS 18001 et définit les exigences pour un système de management de la SST.

Nos services :
- Évaluation des risques professionnels
- Mise en place du système SST
- Formation et sensibilisation
- Préparation à la certification
- Accompagnement continu''',
            'category': qhse_cat,
            'icon': 'fas fa-hard-hat',
            'price_starting_from': 5500.00,
            'duration': '6-12 mois',
            'featured': True,
            'order': 3
        },
        {
            'name': 'Certification ISO 22000',
            'slug': 'certification-iso-22000',
            'short_description': 'Système de management de la sécurité des denrées alimentaires',
            'full_description': '''ISO 22000 est la norme pour la sécurité alimentaire dans toute la chaîne alimentaire.

Nous proposons :
- Analyse des dangers (HACCP)
- Mise en place du système de sécurité alimentaire
- Formation des équipes
- Préparation à la certification
- Audit et amélioration continue''',
            'category': qhse_cat,
            'icon': 'fas fa-utensils',
            'price_starting_from': 6500.00,
            'duration': '6-12 mois',
            'featured': True,
            'order': 4
        },
        {
            'name': 'Certification ISO 27001',
            'slug': 'certification-iso-27001',
            'short_description': 'Système de management de la sécurité de l\'information',
            'full_description': '''ISO 27001 est la norme pour la sécurité de l'information.

Notre accompagnement :
- Analyse des risques informatiques
- Mise en place du SMSI
- Politiques et procédures de sécurité
- Formation et sensibilisation
- Préparation à la certification''',
            'category': qhse_cat,
            'icon': 'fas fa-lock',
            'price_starting_from': 7000.00,
            'duration': '6-12 mois',
            'featured': True,
            'order': 5
        },
    ]
    
    for service_data in services_qhse:
        Service.objects.get_or_create(
            slug=service_data['slug'],
            defaults=service_data
        )
    
    # 3. Services Informatique
    print("3. Création des services Informatique...")
    services_info = [
        {
            'name': 'Audit de cybersécurité',
            'slug': 'audit-cybersecurite',
            'short_description': 'Évaluation complète de votre sécurité informatique',
            'full_description': '''Notre audit de cybersécurité permet d'identifier les vulnérabilités de votre système d'information.

Nous réalisons :
- Audit technique (pentest, scan de vulnérabilités)
- Audit organisationnel (politiques, procédures)
- Analyse des risques
- Rapport détaillé avec recommandations
- Plan d'action priorisé''',
            'category': info_cat,
            'icon': 'fas fa-shield-alt',
            'price_starting_from': 3000.00,
            'duration': '2-4 semaines',
            'featured': True,
            'order': 1
        },
        {
            'name': 'Intelligence Artificielle',
            'slug': 'intelligence-artificielle',
            'short_description': 'Solutions d\'IA sur mesure pour votre entreprise',
            'full_description': '''Nous développons des solutions d'intelligence artificielle adaptées à vos besoins.

Nos services :
- Analyse de vos besoins métier
- Développement de modèles d'IA
- Intégration dans vos processus
- Formation des équipes
- Maintenance et évolution''',
            'category': info_cat,
            'icon': 'fas fa-brain',
            'price_starting_from': 10000.00,
            'duration': '3-6 mois',
            'featured': True,
            'order': 2
        },
        {
            'name': 'Développement d\'applications',
            'slug': 'developpement-applications',
            'short_description': 'Développement d\'applications web et mobiles sur mesure',
            'full_description': '''Nous créons des applications web et mobiles modernes et performantes.

Nos compétences :
- Applications web (React, Django, etc.)
- Applications mobiles (iOS, Android)
- APIs REST
- Bases de données
- Déploiement et maintenance''',
            'category': info_cat,
            'icon': 'fas fa-mobile-alt',
            'price_starting_from': 8000.00,
            'duration': '2-6 mois',
            'featured': True,
            'order': 3
        },
        {
            'name': 'Formation informatique',
            'slug': 'formation-informatique',
            'short_description': 'Formations en cybersécurité, développement et outils numériques',
            'full_description': '''Nous proposons des formations adaptées à vos besoins.

Formations disponibles :
- Cybersécurité (sensibilisation, bonnes pratiques)
- Développement web et mobile
- Outils de collaboration
- Gestion de projet agile
- Cloud computing''',
            'category': info_cat,
            'icon': 'fas fa-chalkboard-teacher',
            'price_starting_from': 1500.00,
            'duration': '1-5 jours',
            'featured': True,
            'order': 4
        },
    ]
    
    for service_data in services_info:
        Service.objects.get_or_create(
            slug=service_data['slug'],
            defaults=service_data
        )
    
    # 4. Certifications
    print("4. Création des certifications...")
    certifications = [
        {'name': 'ISO 9001', 'code': 'ISO 9001', 'category': qhse_cat, 'order': 1},
        {'name': 'ISO 14001', 'code': 'ISO 14001', 'category': qhse_cat, 'order': 2},
        {'name': 'ISO 45001', 'code': 'ISO 45001', 'category': qhse_cat, 'order': 3},
        {'name': 'ISO 22000', 'code': 'ISO 22000', 'category': qhse_cat, 'order': 4},
        {'name': 'ISO 27001', 'code': 'ISO 27001', 'category': qhse_cat, 'order': 5},
    ]
    
    for cert_data in certifications:
        Certification.objects.get_or_create(
            code=cert_data['code'],
            defaults=cert_data
        )
    
    # 5. Témoignages
    print("5. Création des témoignages...")
    testimonials = [
        {
            'client_name': 'Jean Dupont',
            'client_position': 'Directeur Qualité',
            'client_company': 'TechCorp',
            'content': 'Uranus Group nous a accompagnés dans notre certification ISO 9001. Leur expertise et leur professionnalisme ont été remarquables. Nous recommandons vivement leurs services.',
            'rating': 5,
            'featured': True,
            'order': 1
        },
        {
            'client_name': 'Marie Martin',
            'client_position': 'DSI',
            'client_company': 'Innovate Solutions',
            'content': 'L\'audit de cybersécurité réalisé par Uranus Group nous a permis d\'identifier et de corriger des vulnérabilités critiques. Excellent travail !',
            'rating': 5,
            'featured': True,
            'order': 2
        },
        {
            'client_name': 'Pierre Durand',
            'client_position': 'Directeur Général',
            'client_company': 'GreenTech',
            'content': 'Nous avons fait appel à Uranus Group pour notre certification ISO 14001. Leur accompagnement a été parfait du début à la fin.',
            'rating': 5,
            'featured': True,
            'order': 3
        },
    ]
    
    for test_data in testimonials:
        Testimonial.objects.get_or_create(
            client_name=test_data['client_name'],
            defaults=test_data
        )
    
    # 6. Catégories de blog
    print("6. Création des catégories de blog...")
    blog_categories = [
        {'name': 'QHSE', 'slug': 'qhse', 'order': 1},
        {'name': 'Informatique', 'slug': 'informatique', 'order': 2},
        {'name': 'Actualités', 'slug': 'actualites', 'order': 3},
    ]
    
    for cat_data in blog_categories:
        Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
    
    # 7. Articles de blog
    print("7. Création des articles de blog...")
    admin_user = User.objects.filter(is_superuser=True).first()
    if admin_user:
        qhse_category = Category.objects.filter(slug='qhse').first()
        info_category = Category.objects.filter(slug='informatique').first()
        
        articles = [
            {
                'title': 'Les avantages de la certification ISO 9001',
                'slug': 'avantages-certification-iso-9001',
                'excerpt': 'Découvrez pourquoi la certification ISO 9001 est un atout majeur pour votre entreprise.',
                'content': '''La certification ISO 9001 est bien plus qu'un simple label. Elle représente un engagement envers l'excellence et l'amélioration continue.

## Les principaux avantages

### 1. Amélioration de la qualité
Un système de management de la qualité bien implémenté permet de réduire les erreurs et d'améliorer la satisfaction client.

### 2. Accès aux marchés
De nombreux appels d'offres exigent la certification ISO 9001. Elle ouvre de nouvelles opportunités commerciales.

### 3. Optimisation des processus
L'approche processus permet d'identifier et d'éliminer les gaspillages, améliorant ainsi la productivité.

### 4. Image de marque
La certification renforce votre image de marque et votre crédibilité auprès de vos clients et partenaires.

Contactez-nous pour en savoir plus sur notre accompagnement à la certification ISO 9001.''',
                'author': admin_user,
                'category': qhse_category,
                'status': 'published',
                'featured': True,
            },
            {
                'title': 'Cybersécurité : les 10 bonnes pratiques essentielles',
                'slug': 'cybersecurite-bonnes-pratiques',
                'excerpt': 'Protégez votre entreprise avec ces 10 bonnes pratiques de cybersécurité.',
                'content': '''La cybersécurité est devenue un enjeu majeur pour toutes les entreprises. Voici 10 bonnes pratiques essentielles.

## 1. Mots de passe forts
Utilisez des mots de passe complexes et uniques pour chaque compte. Activez l'authentification à deux facteurs.

## 2. Mises à jour régulières
Maintenez vos systèmes et logiciels à jour pour corriger les vulnérabilités.

## 3. Sauvegardes
Effectuez des sauvegardes régulières de vos données critiques.

## 4. Formation des utilisateurs
Sensibilisez vos équipes aux risques de phishing et aux bonnes pratiques.

## 5. Pare-feu et antivirus
Protégez vos systèmes avec des solutions de sécurité adaptées.

Et 5 autres bonnes pratiques dans notre guide complet...''',
                'author': admin_user,
                'category': info_category,
                'status': 'published',
                'featured': True,
            },
        ]
        
        for article_data in articles:
            Article.objects.get_or_create(
                slug=article_data['slug'],
                defaults=article_data
            )
    
    # 8. Slider items
    print("8. Création des items du slider...")
    slider_items = [
        {
            'title': 'Uranus Group',
            'subtitle': 'Expert en QHSE & Informatique',
            'description': 'Accompagnement professionnel pour vos certifications ISO et solutions IT',
            'button_text': 'Découvrir nos services',
            'button_link': '/services/',
            'active': True,
            'order': 1
        },
        {
            'title': 'Certifications ISO',
            'subtitle': '9001, 14001, 45001, 22000, 27001...',
            'description': 'Nous vous accompagnons dans l\'obtention de vos certifications ISO',
            'button_text': 'En savoir plus',
            'button_link': '/services/?category=qhse',
            'active': True,
            'order': 2
        },
        {
            'title': 'Solutions Informatiques',
            'subtitle': 'Cybersécurité, IA, Développement',
            'description': 'Des solutions IT modernes pour votre entreprise',
            'button_text': 'Découvrir',
            'button_link': '/services/?category=informatique',
            'active': True,
            'order': 3
        },
    ]
    
    for item_data in slider_items:
        SliderItem.objects.get_or_create(
            title=item_data['title'],
            defaults=item_data
        )
    
    # 9. Membres de l'équipe
    print("9. Création des membres de l'équipe...")
    team_members = [
        {
            'name': 'Sophie Laurent',
            'position': 'Directrice QHSE',
            'bio': '15 ans d\'expérience en management de la qualité et certifications ISO',
            'order': 1
        },
        {
            'name': 'Thomas Bernard',
            'position': 'Directeur Informatique',
            'bio': 'Expert en cybersécurité et développement d\'applications',
            'order': 2
        },
        {
            'name': 'Julie Moreau',
            'position': 'Consultante QHSE',
            'bio': 'Spécialiste en systèmes de management environnemental',
            'order': 3
        },
    ]
    
    for member_data in team_members:
        TeamMember.objects.get_or_create(
            name=member_data['name'],
            defaults=member_data
        )
    
    print("\n✅ Données de test créées avec succès !")
    print(f"   - {ServiceCategory.objects.count()} catégories de services")
    print(f"   - {Service.objects.count()} services")
    print(f"   - {Certification.objects.count()} certifications")
    print(f"   - {Testimonial.objects.count()} témoignages")
    print(f"   - {Category.objects.count()} catégories de blog")
    print(f"   - {Article.objects.count()} articles")
    print(f"   - {SliderItem.objects.count()} items de slider")
    print(f"   - {TeamMember.objects.count()} membres de l'équipe")

if __name__ == '__main__':
    create_test_data()

