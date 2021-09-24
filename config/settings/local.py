from .base import *  # NOQA
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='3&-!ch9-g%0w$eu3!()qr)6oy4hdq_t#$e*2rdwq1ya18+nop0')
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA


# django-extensions
INSTALLED_APPS += ['django_extensions']  # noqa F405
