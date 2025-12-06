"""
Audit de sécurité automatisé pour Uranus Group
Vérifie la configuration et les bonnes pratiques
"""
import os
import sys
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uranusgroup.settings')
django.setup()


class SecurityAudit:
    """Audit de sécurité de la configuration Django"""

    def __init__(self):
        self.issues = []
        self.warnings = []
        self.passed = []

    def check_debug_mode(self):
        """Vérifier que DEBUG est désactivé en production"""
        if settings.DEBUG:
            self.issues.append({
                'severity': 'HIGH',
                'check': 'DEBUG Mode',
                'issue': 'DEBUG est activé. Désactivez-le en production.',
                'recommendation': 'Mettre DEBUG = False dans settings_production.py'
            })
        else:
            self.passed.append('DEBUG est correctement désactivé')

    def check_secret_key(self):
        """Vérifier la sécurité de SECRET_KEY"""
        secret_key = settings.SECRET_KEY

        if 'django-insecure' in secret_key:
            self.issues.append({
                'severity': 'CRITICAL',
                'check': 'SECRET_KEY',
                'issue': 'SECRET_KEY utilise la valeur par défaut insecure',
                'recommendation': 'Générez une nouvelle clé avec: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"'
            })
        elif len(secret_key) < 50:
            self.warnings.append({
                'severity': 'MEDIUM',
                'check': 'SECRET_KEY',
                'issue': 'SECRET_KEY est trop courte',
                'recommendation': 'Utilisez une clé d\'au moins 50 caractères'
            })
        else:
            self.passed.append('SECRET_KEY semble sécurisée')

    def check_allowed_hosts(self):
        """Vérifier ALLOWED_HOSTS"""
        if '*' in settings.ALLOWED_HOSTS:
            self.issues.append({
                'severity': 'HIGH',
                'check': 'ALLOWED_HOSTS',
                'issue': 'ALLOWED_HOSTS contient "*" (tous les hosts autorisés)',
                'recommendation': 'Spécifiez explicitement les domaines autorisés'
            })
        elif not settings.ALLOWED_HOSTS:
            self.issues.append({
                'severity': 'HIGH',
                'check': 'ALLOWED_HOSTS',
                'issue': 'ALLOWED_HOSTS est vide',
                'recommendation': 'Configurez ALLOWED_HOSTS avec vos domaines'
            })
        else:
            self.passed.append('ALLOWED_HOSTS est correctement configuré')

    def check_csrf_protection(self):
        """Vérifier la protection CSRF"""
        if 'django.middleware.csrf.CsrfViewMiddleware' not in settings.MIDDLEWARE:
            self.issues.append({
                'severity': 'CRITICAL',
                'check': 'CSRF Protection',
                'issue': 'Middleware CSRF non activé',
                'recommendation': 'Ajoutez django.middleware.csrf.CsrfViewMiddleware à MIDDLEWARE'
            })
        else:
            self.passed.append('Protection CSRF activée')

    def check_security_headers(self):
        """Vérifier les headers de sécurité"""
        checks = {
            'SECURE_BROWSER_XSS_FILTER': getattr(settings, 'SECURE_BROWSER_XSS_FILTER', False),
            'SECURE_CONTENT_TYPE_NOSNIFF': getattr(settings, 'SECURE_CONTENT_TYPE_NOSNIFF', False),
            'X_FRAME_OPTIONS': getattr(settings, 'X_FRAME_OPTIONS', None),
        }

        if not checks['SECURE_BROWSER_XSS_FILTER']:
            self.warnings.append({
                'severity': 'MEDIUM',
                'check': 'Security Headers',
                'issue': 'SECURE_BROWSER_XSS_FILTER non activé',
                'recommendation': 'Activez SECURE_BROWSER_XSS_FILTER = True'
            })

        if not checks['SECURE_CONTENT_TYPE_NOSNIFF']:
            self.warnings.append({
                'severity': 'MEDIUM',
                'check': 'Security Headers',
                'issue': 'SECURE_CONTENT_TYPE_NOSNIFF non activé',
                'recommendation': 'Activez SECURE_CONTENT_TYPE_NOSNIFF = True'
            })

        if checks['X_FRAME_OPTIONS'] != 'DENY':
            self.warnings.append({
                'severity': 'MEDIUM',
                'check': 'Security Headers',
                'issue': 'X_FRAME_OPTIONS n\'est pas défini à DENY',
                'recommendation': 'Définissez X_FRAME_OPTIONS = "DENY"'
            })

        if all(checks.values()):
            self.passed.append('Headers de sécurité configurés')

    def check_https_settings(self):
        """Vérifier les paramètres HTTPS"""
        if not settings.DEBUG:
            https_settings = {
                'SECURE_SSL_REDIRECT': getattr(settings, 'SECURE_SSL_REDIRECT', False),
                'SESSION_COOKIE_SECURE': getattr(settings, 'SESSION_COOKIE_SECURE', False),
                'CSRF_COOKIE_SECURE': getattr(settings, 'CSRF_COOKIE_SECURE', False),
            }

            if not https_settings['SECURE_SSL_REDIRECT']:
                self.issues.append({
                    'severity': 'HIGH',
                    'check': 'HTTPS',
                    'issue': 'SECURE_SSL_REDIRECT non activé',
                    'recommendation': 'Activez SECURE_SSL_REDIRECT = True en production'
                })

            if not https_settings['SESSION_COOKIE_SECURE']:
                self.issues.append({
                    'severity': 'HIGH',
                    'check': 'HTTPS',
                    'issue': 'SESSION_COOKIE_SECURE non activé',
                    'recommendation': 'Activez SESSION_COOKIE_SECURE = True en production'
                })

            if not https_settings['CSRF_COOKIE_SECURE']:
                self.issues.append({
                    'severity': 'HIGH',
                    'check': 'HTTPS',
                    'issue': 'CSRF_COOKIE_SECURE non activé',
                    'recommendation': 'Activez CSRF_COOKIE_SECURE = True en production'
                })

            if all(https_settings.values()):
                self.passed.append('Paramètres HTTPS correctement configurés')

    def check_password_validators(self):
        """Vérifier les validateurs de mot de passe"""
        if not settings.AUTH_PASSWORD_VALIDATORS:
            self.issues.append({
                'severity': 'HIGH',
                'check': 'Password Validators',
                'issue': 'Aucun validateur de mot de passe configuré',
                'recommendation': 'Configurez AUTH_PASSWORD_VALIDATORS'
            })
        else:
            self.passed.append('Validateurs de mot de passe configurés')

    def check_database_security(self):
        """Vérifier la sécurité de la base de données"""
        db_config = settings.DATABASES['default']

        if db_config['ENGINE'] == 'django.db.backends.sqlite3':
            if not settings.DEBUG:
                self.warnings.append({
                    'severity': 'MEDIUM',
                    'check': 'Database',
                    'issue': 'SQLite utilisé en production',
                    'recommendation': 'Utilisez PostgreSQL en production'
                })
        else:
            self.passed.append('Base de données de production configurée')

    def check_logging(self):
        """Vérifier la configuration du logging"""
        if not hasattr(settings, 'LOGGING') or not settings.LOGGING:
            if not settings.DEBUG:
                self.warnings.append({
                    'severity': 'LOW',
                    'check': 'Logging',
                    'issue': 'Logging non configuré',
                    'recommendation': 'Configurez le logging pour la production'
                })
        else:
            self.passed.append('Logging configuré')

    def check_cors_settings(self):
        """Vérifier la configuration CORS"""
        if hasattr(settings, 'CORS_ALLOW_ALL_ORIGINS'):
            if settings.CORS_ALLOW_ALL_ORIGINS and not settings.DEBUG:
                self.issues.append({
                    'severity': 'HIGH',
                    'check': 'CORS',
                    'issue': 'CORS_ALLOW_ALL_ORIGINS activé en production',
                    'recommendation': 'Désactivez CORS_ALLOW_ALL_ORIGINS et configurez CORS_ALLOWED_ORIGINS'
                })
            else:
                self.passed.append('CORS correctement configuré')

    def run_audit(self):
        """Exécuter tous les audits"""
        print("="*70)
        print("AUDIT DE SÉCURITÉ - URANUS GROUP")
        print("="*70)
        print()

        self.check_debug_mode()
        self.check_secret_key()
        self.check_allowed_hosts()
        self.check_csrf_protection()
        self.check_security_headers()
        self.check_https_settings()
        self.check_password_validators()
        self.check_database_security()
        self.check_logging()
        self.check_cors_settings()

        self.print_report()

    def print_report(self):
        """Afficher le rapport d'audit"""
        print("\n" + "="*70)
        print("RAPPORT D'AUDIT")
        print("="*70)

        # Problèmes critiques
        critical = [i for i in self.issues if i['severity'] == 'CRITICAL']
        if critical:
            print("\n🔴 PROBLÈMES CRITIQUES:")
            for issue in critical:
                print(f"\n  [{issue['severity']}] {issue['check']}")
                print(f"  Problème: {issue['issue']}")
                print(f"  Recommandation: {issue['recommendation']}")

        # Problèmes élevés
        high = [i for i in self.issues if i['severity'] == 'HIGH']
        if high:
            print("\n🟠 PROBLÈMES ÉLEVÉS:")
            for issue in high:
                print(f"\n  [{issue['severity']}] {issue['check']}")
                print(f"  Problème: {issue['issue']}")
                print(f"  Recommandation: {issue['recommendation']}")

        # Avertissements
        if self.warnings:
            print("\n🟡 AVERTISSEMENTS:")
            for warning in self.warnings:
                print(f"\n  [{warning['severity']}] {warning['check']}")
                print(f"  Problème: {warning['issue']}")
                print(f"  Recommandation: {warning['recommendation']}")

        # Tests réussis
        if self.passed:
            print("\n✅ TESTS RÉUSSIS:")
            for check in self.passed:
                print(f"  ✓ {check}")

        # Résumé
        print("\n" + "="*70)
        print("RÉSUMÉ")
        print("="*70)
        print(f"Problèmes critiques: {len(critical)}")
        print(f"Problèmes élevés: {len(high)}")
        print(f"Avertissements: {len(self.warnings)}")
        print(f"Tests réussis: {len(self.passed)}")
        print("="*70)

        # Score de sécurité
        total_checks = len(self.issues) + len(self.warnings) + len(self.passed)
        if total_checks > 0:
            score = (len(self.passed) / total_checks) * 100
            print(f"\nScore de sécurité: {score:.1f}%")
            if score >= 80:
                print("✅ Niveau de sécurité: BON")
            elif score >= 60:
                print("⚠️  Niveau de sécurité: MOYEN")
            else:
                print("🔴 Niveau de sécurité: FAIBLE")


if __name__ == '__main__':
    audit = SecurityAudit()
    audit.run_audit()

