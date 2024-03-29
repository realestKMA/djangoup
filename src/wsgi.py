"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from src import env

from django.core.wsgi import get_wsgi_application

if env.APP_ENVIRONMENT == "development":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.production")

application = get_wsgi_application()
