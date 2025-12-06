"""
Health check endpoint pour monitoring
"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import connection
from django.core.cache import cache

try:
    import redis
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False


@require_http_methods(["GET"])
def health_check(request):
    """
    Endpoint de health check pour monitoring
    """
    health_status = {
        'status': 'healthy',
        'checks': {}
    }
    
    # Vérifier la base de données
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            health_status['checks']['database'] = 'ok'
    except Exception as e:
        health_status['checks']['database'] = f'error: {str(e)}'
        health_status['status'] = 'unhealthy'
    
    # Vérifier le cache Redis
    try:
        cache.set('health_check', 'ok', 10)
        if cache.get('health_check') == 'ok':
            health_status['checks']['cache'] = 'ok'
        else:
            health_status['checks']['cache'] = 'error: cache not working'
            health_status['status'] = 'degraded'
    except Exception as e:
        health_status['checks']['cache'] = f'error: {str(e)}'
        health_status['status'] = 'degraded'
    
    # Vérifier Redis directement (optionnel)
    if REDIS_AVAILABLE:
        try:
            r = redis.Redis(host='localhost', port=6379, db=1, socket_connect_timeout=1)
            r.ping()
            health_status['checks']['redis'] = 'ok'
        except Exception as e:
            health_status['checks']['redis'] = f'error: {str(e)}'
            health_status['status'] = 'degraded'
    else:
        health_status['checks']['redis'] = 'not_configured'
    
    status_code = 200 if health_status['status'] == 'healthy' else 503
    
    return JsonResponse(health_status, status=status_code)

