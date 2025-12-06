"""
Configuration Gunicorn pour la production
"""
import multiprocessing
import os

# Nombre de workers (recommandé: 2-4 x nombre de CPU)
workers = multiprocessing.cpu_count() * 2 + 1

# Nombre de threads par worker
threads = 2

# Bind
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"

# Timeout
timeout = 120
keepalive = 5

# Logging
accesslog = os.path.join(os.path.dirname(__file__), 'logs', 'gunicorn_access.log')
errorlog = os.path.join(os.path.dirname(__file__), 'logs', 'gunicorn_error.log')
loglevel = 'info'

# Process naming
proc_name = 'uranusgroup'

# User et group (à configurer selon votre serveur)
# user = 'www-data'
# group = 'www-data'

# Daemon mode (décommentez pour lancer en arrière-plan)
# daemon = True
# pidfile = '/var/run/gunicorn/uranusgroup.pid'

# Preload app
preload_app = True

# Worker class
worker_class = 'sync'

# Max requests (reload workers après N requests pour éviter les fuites mémoire)
max_requests = 1000
max_requests_jitter = 50

