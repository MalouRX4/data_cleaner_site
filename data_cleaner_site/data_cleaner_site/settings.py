import os

ALLOWED_HOSTS = ['*']  # Accepte toutes les connexions

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Et commente ou désactive DEBUG = False (garde-le à True au début).
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-xyz'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'data_cleaner',
]

MIDDLEWARE = []
ROOT_URLCONF = 'data_cleaner_site.urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
               'DIRS': [],
               'APP_DIRS': True,
               'OPTIONS': {'context_processors': []},
}]
WSGI_APPLICATION = 'data_cleaner_site.wsgi.application'
STATIC_URL = '/static/'
