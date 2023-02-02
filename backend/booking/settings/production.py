from . import base  # noqa
from .base import env

SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
base.DATABASES['default'] = env.db('DATABASE_URL')
DEBUG = env.bool('DJANGO_DEBUG')
