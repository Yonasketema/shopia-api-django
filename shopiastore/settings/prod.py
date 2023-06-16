import os
import dj_database_url
from .base import *

DEBUG = False


SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ["shopia-api-django-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ['https://shopia-api-django-production.up.railway.app']
