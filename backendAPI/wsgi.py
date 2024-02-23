"""
WSGI config for backendAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

DEBUG = os.environ.get('DEBUG')

if not DEBUG:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backendAPI.production_settings')
else:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backendAPI.settings')

application = get_wsgi_application()
