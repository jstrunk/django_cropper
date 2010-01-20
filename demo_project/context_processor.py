from django.conf import settings

def static_url(request):
    
    # The URL path to STATIC_ROOT
    URL = getattr(settings, 'STATIC_URL', '')
    
    return {'STATIC_URL': URL}


