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
SECRET_KEY = "CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead)."

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    ".herokuapp.com"
]

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

