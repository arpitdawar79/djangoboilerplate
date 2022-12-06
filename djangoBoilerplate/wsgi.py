"""
WSGI config for djangoBoilerplate project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoBoilerplate.settings")
if os.getenv('MODE') == 'PROD':
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')
else:
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

from configurations.wsgi import get_wsgi_application  # noqa
application = get_wsgi_application()
