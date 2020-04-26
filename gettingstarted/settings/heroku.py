#
# Filename: heroku.py
# Project : Clock My Time
#
# Created by Tu Tong on 04/12/20
# Copyright 2020 Tu Tong. All rights reserved.
#

from gettingstarted.settings.base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    ".herokuapp.com"
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

WSGI_APPLICATION = "gettingstarted.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

APP_SQL_ENGINE = os.environ.get("APP_SQL_ENGINE")
APP_SQL_NAME = os.environ.get("APP_SQL_NAME")
APP_SQL_USER = os.environ.get("APP_SQL_USER")
APP_SQL_PASS = os.environ.get("APP_SQL_PASS")
APP_SQL_HOST = os.environ.get("APP_SQL_HOST")
APP_SQL_PORT = os.environ.get("APP_SQL_PORT")

DATABASES = {
    "default": {
        "ENGINE" : APP_SQL_ENGINE,
        "NAME": APP_SQL_NAME,
        "USER": APP_SQL_USER,
        "PASSWORD": APP_SQL_PASS,
        "HOST": APP_SQL_HOST,
        "PORT": APP_SQL_PORT
    }
}

# https://github.com/adamchainz/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'https://clock-my-time.azurewebsites.net',
    'https://scottflaskapptutorial.herokuapp.com'
)

CSRF_TRUSTED_ORIGINS = ['scottflaskapptutorial.herokuapp.com', 'clock-my-time.azurewebsites.net']

SESSION_COOKIE_DOMAIN = "clock-my-time.azurewebsites.net"