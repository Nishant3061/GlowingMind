# -*-coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Standard Library
import datetime
import os
from os.path import dirname, join

# Third Paryt Stuff
from django.conf.global_settings import DEBUG  # noqa
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(ROOT_DIR, ...)
ROOT_DIR = dirname(dirname(__file__))
APP_DIR = join(ROOT_DIR, 'GlowingMind')

# General project information
# These are available in the template as SITE_INFO.<title>
dt = datetime.datetime.now()
SITE_VARIABLES = {
    'site_name': os.environ.get('SITE_NAME', 'GlowingMind'),
    'site_description': 'It is a moodle where any one can attempt various ' +
                        'tests and track there performance',
    'footer': '&copy; {} • GlowingMind Pvt Ltd'.format(dt.year),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

SITE_ID = 1

OUR_APPS = [
]

INSTALLED_APPS = CORE_APPS + THIRD_PARTY_APPS + OUR_APPS


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APP_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'GlowingMind.base.context_processors.site_info',
            ],
            # 'loaders': [
            #  (
            #     'django.template.loaders.filesystem.Loader',
            #     [os.path.join(APP_DIR, 'templates')],
            #  ),
            # ],

            'debug': DEBUG,
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# ******************************************************************************
#                   django-allauth settings
# ******************************************************************************

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[{}] ".format(SITE_VARIABLES['site_name'])
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_SIGNUP_FORM_CLASS = 'GlowingMind.forms.SignupForm'

LOGIN_REDIRECT_URL = '/home'
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login"


# *********************django-allauth settings end*****************************


# E-mail settings
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LANGUAGES = (
    ("en", _("English")),
)

ROOT_URLCONF = 'GlowingMind.urls'
WSGI_APPLICATION = 'wsgi.application'

# Internationalization

ATOMIC_REQUESTS = True
TIME_ZONE = 'Asia/Kolkata'
LANGUAGE_CODE = "en"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_DIR, 'assests', 'collected-static')
STATICFILES_DIRS = (
    os.path.join(APP_DIR, 'static'),
)

MEDIA_ROOT = join(ROOT_DIR, '.media')
MEDIA_URL = '/m/'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME_G', ''),
        'USER': os.environ.get('DB_USER_G', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '$yzkd%dd_&i=gc$c+ld&3q-ik$a4=)po4v&(2zyocro8x4h0!f')

ALLOWED_HOSTS = []  # TODO:

SITE_PROTOCOL = 'http'

# Add connection life time
# Make sure DB request held on for minimim 5 minutes
CONN_MAX_AGE = 300


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation' +
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation' +
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation' +
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation' +
                '.NumericPasswordValidator',
    },
]
