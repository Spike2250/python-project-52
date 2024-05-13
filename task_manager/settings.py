"""
Django settings for task_manager project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')
ON_RENDER = os.getenv('ON_RENDER', False)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')
DEBUG = True if DEBUG and DEBUG != '0' else False

ROLLBAR_ACCESS_TOKEN = os.getenv("ROLLBAR_ACCESS_TOKEN")
ROLLBAR = {
    'access_token': ROLLBAR_ACCESS_TOKEN,
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}

ALLOWED_HOSTS = [
    'webserver',
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
    '.onrender.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'task_manager',
    'task_manager.users.apps.UsersConfig',
    # 'task_manager.users',
    'task_manager.statuses',
    'task_manager.tasks',
    'task_manager.labels',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'task_manager.wsgi.application'

CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com'
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


if ON_RENDER:
    DATABASE = dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600
    )
else:
    DATABASE = dj_database_url.parse(f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
DATABASES = {'default': DATABASE}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

valid = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{valid}.UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{valid}.MinimumLengthValidator',
    },
    {
        'NAME': f'{valid}.CommonPasswordValidator',
    },
    {
        'NAME': f'{valid}.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en-us', 'English'),
    ('ru-ru', 'Russian'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
