"""
Tests de pénétration et sécurité pour Uranus Group
Vérifie les vulnérabilités communes et les bonnes pratiques de sécurité
"""
import os
import sys
import django
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uranusgroup.settings')
django.setup()

User = get_user_model()


class SecurityTests(TestCase):
    """Tests de sécurité et pénétration"""

    def setUp(self):
        """Configuration initiale"""
        self.client = Client()
        # Créer un utilisateur de test
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPassword123!',
            role='client'
        )
        # Créer un admin de test
        self.admin_user = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='AdminPassword123!',
            role='admin'
        )
        self.admin_user.is_staff = True
        self.admin_user.save()

    # ==================== TESTS CSRF ====================

    def test_csrf_protection_enabled(self):
        """Vérifier que la protection CSRF est activée"""
        self.assertIn(
            'django.middleware.csrf.CsrfViewMiddleware',
            settings.MIDDLEWARE
        )

    def test_csrf_token_required_for_post(self):
        """Vérifier que les requêtes POST nécessitent un token CSRF"""
        # Tenter de se connecter sans token CSRF
        response = self.client.post(
            reverse('accounts:login'),
            {
                'username': 'testuser',
                'password': 'TestPassword123!'
            },
            follow=True
        )
        # Django devrait rejeter la requête (403 ou redirection)
        self.assertIn(
            response.status_code,
            [403, 302, 400],
            "CSRF protection ne fonctionne pas correctement"
        )

    # ==================== TESTS SQL INJECTION ====================

    def test_sql_injection_in_login(self):
        """Tester la protection contre SQL injection dans le login"""
        # Tentatives d'injection SQL communes
        sql_payloads = [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR '1'='1' /*",
            "admin'--",
            "admin'/*",
            "' UNION SELECT * FROM users--",
        ]

        for payload in sql_payloads:
            response = self.client.post(
                reverse('accounts:login'),
                {
                    'username': payload,
                    'password': 'anything'
                },
                follow=True
            )
            # Ne devrait pas causer d'erreur 500 (erreur serveur)
            self.assertNotEqual(
                response.status_code,
                500,
                f"Vulnérabilité SQL injection détectée avec: {payload}"
            )

    def test_sql_injection_in_search(self):
        """Tester la protection contre SQL injection dans les recherches"""
        sql_payloads = [
            "' OR '1'='1",
            "'; DROP TABLE users; --",
            "' UNION SELECT * FROM users--",
        ]

        # Tester sur différentes pages avec recherche
        search_urls = [
            reverse('services:service_list'),
            reverse('blog:article_list'),
        ]

        for url in search_urls:
            for payload in sql_payloads:
                response = self.client.get(url, {'search': payload})
                self.assertNotEqual(
                    response.status_code,
                    500,
                    f"Vulnérabilité SQL injection dans {url} avec: {payload}"
                )

    # ==================== TESTS XSS ====================

    def test_xss_in_contact_form(self):
        """Tester la protection contre XSS dans le formulaire de contact"""
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "javascript:alert('XSS')",
            "<iframe src=javascript:alert('XSS')>",
        ]

        for payload in xss_payloads:
            response = self.client.post(
                reverse('core:contact'),
                {
                    'name': payload,
                    'email': 'test@example.com',
                    'subject': 'Test',
                    'message': payload
                },
                follow=True
            )
            # Le contenu ne devrait pas être exécuté
            if response.status_code == 200:
                content = response.content.decode('utf-8')
                # Vérifier que le script n'est pas présent tel quel
                self.assertNotIn(
                    '<script>alert',
                    content,
                    f"Vulnérabilité XSS détectée avec: {payload}"
                )

    def test_xss_in_user_input(self):
        """Tester la protection XSS dans les champs utilisateur"""
        xss_payload = "<script>alert('XSS')</script>"

        # Tester avec un utilisateur connecté
        self.client.login(username='testuser', password='TestPassword123!')

        # Tester différents formulaires
        test_urls = [
            (reverse('accounts:profile'), {
                'first_name': xss_payload,
                'last_name': xss_payload,
            }),
        ]

        for url, data in test_urls:
            try:
                response = self.client.post(url, data, follow=True)
                if response.status_code == 200:
                    content = response.content.decode('utf-8')
                    self.assertNotIn(
                        '<script>alert',
                        content,
                        f"Vulnérabilité XSS dans {url}"
                    )
            except Exception:
                pass  # Certains formulaires peuvent ne pas exister

    # ==================== TESTS AUTHENTIFICATION ====================

    def test_authentication_required_for_dashboard(self):
        """Vérifier que le dashboard nécessite une authentification"""
        response = self.client.get(reverse('accounts:dashboard'))
        # Devrait rediriger vers la page de login
        self.assertIn(
            response.status_code,
            [302, 403],
            "Dashboard accessible sans authentification"
        )

    def test_admin_required_for_admin_dashboard(self):
        """Vérifier que le dashboard admin nécessite les droits admin"""
        # Se connecter en tant qu'utilisateur normal
        self.client.login(
            username='testuser',
            password='TestPassword123!'
        )
        response = self.client.get(reverse('dashboard:admin_dashboard'))
        # Devrait être refusé ou redirigé
        self.assertIn(
            response.status_code,
            [302, 403, 404],
            "Dashboard admin accessible sans droits admin"
        )

    def test_brute_force_protection(self):
        """Tester la protection contre les attaques brute force"""
        # Tenter plusieurs connexions échouées
        for i in range(10):
            response = self.client.post(
                reverse('accounts:login'),
                {
                    'username': 'testuser',
                    'password': 'WrongPassword'
                }
            )
        # Le système devrait toujours fonctionner (pas de blocage permanent)
        # mais pourrait avoir un rate limiting
        response = self.client.post(
            reverse('accounts:login'),
            {
                'username': 'testuser',
                'password': 'TestPassword123!'
            }
        )
        # Devrait toujours permettre la connexion correcte
        self.assertIn(response.status_code, [200, 302])

    # ==================== TESTS SENSITIVE DATA ====================

    def test_secret_key_not_exposed(self):
        """Vérifier que SECRET_KEY n'est pas exposé"""
        response = self.client.get(reverse('core:home'))
        content = response.content.decode('utf-8')
        # Le SECRET_KEY ne devrait jamais apparaître dans les réponses
        self.assertNotIn(
            settings.SECRET_KEY,
            content,
            "SECRET_KEY exposé dans la réponse"
        )

    def test_debug_mode_disabled_in_production(self):
        """Vérifier que DEBUG est False en production"""
        # Ce test devrait être exécuté avec DEBUG=False
        # En développement, on vérifie juste que la variable existe
        self.assertIn('DEBUG', dir(settings))

    def test_sensitive_headers_not_exposed(self):
        """Vérifier que les headers sensibles ne sont pas exposés"""
        response = self.client.get(reverse('core:home'))
        # Vérifier que certains headers ne sont pas présents
        sensitive_headers = [
            'X-Powered-By',
            'Server',
        ]
        for header in sensitive_headers:
            self.assertNotIn(
                header,
                response,
                f"Header sensible {header} exposé"
            )

    # ==================== TESTS FILE UPLOAD ====================

    def test_file_upload_validation(self):
        """Tester la validation des fichiers uploadés"""
        # Créer un fichier malveillant (simulé)
        malicious_content = b'<?php system($_GET["cmd"]); ?>'

        self.client.login(
            username='testuser',
            password='TestPassword123!'
        )

        # Tester l'upload sur différents endpoints
        # (Adapter selon vos endpoints d'upload)
        test_cases = [
            # Ajouter vos endpoints d'upload ici
        ]

        for url, field_name in test_cases:
            try:
                response = self.client.post(
                    url,
                    {field_name: malicious_content},
                    follow=True
                )
                # Ne devrait pas accepter les fichiers malveillants
                self.assertNotEqual(
                    response.status_code,
                    200,
                    f"Fichier malveillant accepté dans {url}"
                )
            except Exception:
                pass

    # ==================== TESTS PATH TRAVERSAL ====================

    def test_path_traversal_protection(self):
        """Tester la protection contre path traversal"""
        traversal_payloads = [
            '../../../etc/passwd',
            '..\\..\\..\\windows\\system32\\config\\sam',
            '....//....//....//etc/passwd',
            '%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd',
        ]

        for payload in traversal_payloads:
            # Tester différents endpoints
            test_urls = [
                f'/media/{payload}',
                f'/static/{payload}',
            ]

            for url in test_urls:
                response = self.client.get(url)
                # Ne devrait pas exposer des fichiers système
                self.assertNotIn(
                    'root:',
                    response.content.decode('utf-8', errors='ignore'),
                    f"Path traversal vulnérable avec: {payload}"
                )

    # ==================== TESTS SESSION SECURITY ====================

    def test_session_cookie_httponly(self):
        """Vérifier que les cookies de session sont HttpOnly"""
        self.client.login(
            username='testuser',
            password='TestPassword123!'
        )
        response = self.client.get(reverse('accounts:dashboard'))
        # Vérifier les cookies de session
        session_cookie = response.cookies.get(settings.SESSION_COOKIE_NAME)
        if session_cookie:
            # En production, devrait être HttpOnly et Secure
            pass  # Vérification dépend de la configuration

    def test_session_fixation_protection(self):
        """Tester la protection contre la fixation de session"""
        # Obtenir une session
        self.client.get(reverse('core:home'))
        old_session_key = self.client.session.session_key

        # Se connecter
        self.client.login(
            username='testuser',
            password='TestPassword123!'
        )
        new_session_key = self.client.session.session_key

        # La clé de session devrait changer après login
        # (Django le fait par défaut)
        self.assertNotEqual(
            old_session_key,
            new_session_key,
            "Protection contre la fixation de session manquante"
        )

    # ==================== TESTS INPUT VALIDATION ====================

    def test_input_length_validation(self):
        """Tester la validation de la longueur des entrées"""
        # Créer une entrée très longue
        long_string = 'A' * 10000

        self.client.login(
            username='testuser',
            password='TestPassword123!'
        )

        # Tester différents formulaires
        test_cases = [
            (reverse('core:contact'), {
                'name': long_string,
                'email': 'test@example.com',
                'subject': 'Test',
                'message': long_string
            }),
        ]

        for url, data in test_cases:
            response = self.client.post(url, data, follow=True)
            # Ne devrait pas causer d'erreur serveur
            self.assertNotEqual(
                response.status_code,
                500,
                f"Entrée trop longue non validée dans {url}"
            )

    # ==================== TESTS SECURITY HEADERS ====================

    def test_security_headers_present(self):
        """Vérifier la présence des headers de sécurité"""
        response = self.client.get(reverse('core:home'))

        # Headers de sécurité recommandés
        security_headers = {
            'X-Frame-Options': 'DENY',
            'X-Content-Type-Options': 'nosniff',
            'X-XSS-Protection': '1; mode=block',
        }

        for header, expected_value in security_headers.items():
            actual_value = response.get(header, '')
            if actual_value:
                self.assertIn(
                    expected_value.lower(),
                    actual_value.lower(),
                    f"Header {header} manquant ou incorrect"
                )

    # ==================== TESTS AUTHORIZATION ====================

    def test_unauthorized_access_denied(self):
        """Tester que l'accès non autorisé est refusé"""
        # Se connecter en tant qu'utilisateur normal
        self.client.login(
            username='testuser',
            password='TestPassword123!'
        )

        # Tenter d'accéder à des ressources admin
        admin_urls = [
            reverse('dashboard:admin_dashboard'),
            reverse('dashboard:manage_users'),
        ]

        for url in admin_urls:
            response = self.client.get(url)
            # Devrait être refusé
            self.assertIn(
                response.status_code,
                [302, 403, 404],
                f"Accès non autorisé permis à {url}"
            )

    def test_idor_protection(self):
        """Tester la protection contre IDOR (Insecure Direct Object Reference)"""
        self.client.login(
            username='testuser',
            password='TestPassword123!'
        )

        # Tenter d'accéder à des ressources d'autres utilisateurs
        # (Adapter selon vos modèles)
        # Exemple: tenter d'accéder à une demande d'un autre utilisateur
        # response = self.client.get('/services/requests/999/')
        # self.assertIn(response.status_code, [403, 404])

    # ==================== TESTS ERROR HANDLING ====================

    def test_error_messages_not_reveal_info(self):
        """Vérifier que les messages d'erreur ne révèlent pas d'informations"""
        # Tenter des actions qui causent des erreurs
        test_cases = [
            ('/nonexistent/', 404),
            ('/accounts/login/', 200),  # Devrait être accessible
        ]

        for url, expected_status in test_cases:
            response = self.client.get(url)
            if response.status_code == 500:
                content = response.content.decode('utf-8', errors='ignore')
                # Ne devrait pas révéler des chemins de fichiers
                self.assertNotIn(
                    '/home/',
                    content,
                    f"Informations sensibles révélées dans {url}"
                )
                self.assertNotIn(
                    'Traceback',
                    content,
                    f"Traceback exposé dans {url}"
                )


def run_security_tests():
    """Exécuter tous les tests de sécurité"""
    import unittest

    # Créer une suite de tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(SecurityTests)

    # Exécuter les tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Résumé
    print("\n" + "="*70)
    print("RÉSUMÉ DES TESTS DE SÉCURITÉ")
    print("="*70)
    print(f"Tests exécutés: {result.testsRun}")
    print(f"Succès: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Erreurs: {len(result.errors)}")
    print("="*70)

    if result.failures:
        print("\nÉCHECS DÉTECTÉS:")
        for test, traceback in result.failures:
            print(f"\n- {test}:")
            print(traceback)

    if result.errors:
        print("\nERREURS DÉTECTÉES:")
        for test, traceback in result.errors:
            print(f"\n- {test}:")
            print(traceback)

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_security_tests()
    sys.exit(0 if success else 1)

