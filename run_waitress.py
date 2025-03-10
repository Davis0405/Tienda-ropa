import os
from waitress import serve
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings')
application = get_wsgi_application()

serve(application, host='192.168.0.20', port=8000)