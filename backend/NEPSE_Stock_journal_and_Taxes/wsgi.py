"""
WSGI config for NEPSE_Stock_journal_and_Taxes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NEPSE_Stock_journal_and_Taxes.settings")

application = get_wsgi_application()
