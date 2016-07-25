"""
WSGI config for bias_tracker project.

Updated with DjangoGirls Heroku deployment settings.  I see the incorrect
quote marks, but Django auto-wrote those and I do not know enough to risk
second-guessing the installation choices.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bias_tracker.settings")

application = get_wsgi_application()

application = DjangoWhiteNoise(application)
