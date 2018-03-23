"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l02&+iqwre-u0*8(q0j7cp9l-*7x0sjw5rf3zctrcein34sz!o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'ypfcollection.apps.YpfcollectionConfig',
    # 'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

 # DATABASES = {
     # 'default': {
         # 'ENGINE': 'django.db.backends.sqlite3',
         # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     # }
 # }

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.mysql',
       # 'OPTIONS':{'read_default_file':'c:/wamp64/bin/mysql/mysql5.7.14/wampserver.conf'},
    # }
# }


# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.mysql', 
        # 'NAME': 'polls',
        # 'USER': 'root',
        # 'PASSWORD': '',
        # 'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        # 'PORT': '3306',
    # }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'rickson$ypfcollection',                      # Or path to database file if using 
        # The following settings are not used with sqlite3:
        'USER': 'rickson',
        'PASSWORD': 'drowning',
        'HOST': 'rickson.mysql.pythonanywhere-services.com',                      # Empty for localhost through domain sockets or   '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# PROJECT_NAME = ''
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATICFILES_DIRS = [os.path.join(BASE_DIR, PROJECT_NAME)]
# STATIC_ROOT = os.path.join(BASE_DIR,'', 'staticfiles')
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATICFILES_DIRS = (
  os.path.join(SITE_ROOT, 'static/'),
)
