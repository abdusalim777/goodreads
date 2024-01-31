# from pathlib import Path
# import environ
# import os
# from decouple import config
#
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
#
# LOGIN_URL = 'users:login'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
#
# ALLOWED_HOSTS = ['goodreads.uz', 'www.goodreads.uz', '127.0.0.1']
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#
#     'crispy_forms',
#     'crispy_bootstrap5',
#     'rest_framework',
#     'whitenoise.runserver_nostatic',
#
#     'books',
#     'users',
#     'api',
# ]
#
# CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
# CRISPY_TEMPLATE_PACK = 'bootstrap5'
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#
# ]
#
# ROOT_URLCONF = 'config.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             BASE_DIR / 'templates'
#         ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'config.wsgi.application'
#
# # Database
# # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'HOST': config('HOST'),
#         'PORT': config('PORT'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#
#     }
# }
#
# # Password validation
# # https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# # Internationalization
# # https://docs.djangoproject.com/en/4.0/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_TZ = True
#
# AUTH_USER_MODEL = 'users.CustomUser'
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/home/goodread/goodreads.uz/django/media-files'
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.0/howto/static-files/
#
# STATIC_URL = 'static/'
# STATIC_ROOT = '/home/goodread/goodreads.uz/django/staticfiles'
# STATICFILES_DIRS = ('/home/goodread/goodreads.uz/django/static',)
# # STATICFILES_DIRS = [
# #     BASE_DIR / 'static'
# # ]
#
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_HOST = 'smtp.gmail.com'
# # EMAIL_HOST_USER = 'sayitqulovabdusalimjon@gmail.com'
# # EMAIL_HOST_PASSWORD = '****'
# # EMAIL_PORT = 587
# # EMAIL_USE_TLS = True
# # EMAIL_USE_SSL = False
#
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 2
# }
#
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#
from pathlib import Path
import environ

from decouple import config
import os
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = 'django-insecure-91@54_7e$es@%a&74*f&po19jpux&46#)uzbbmh*tk84f72=^7'

LOGIN_URL = 'users:login'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'crispy_bootstrap5',
    'rest_framework',
    'whitenoise.runserver_nostatic',

    'books',
    'users',
    'api',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Goodreads',
        'HOST': '127.0.0.1',
        'PORT': '5433',
        'USER': 'postgres',
        'PASSWORD': 'abdusalim'

    }
}

import os, dj_database_url

DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.CustomUser'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('media-files')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join('staticfiles')

STATICFILES_DIRS = [
    str(BASE_DIR.joinpath('static'))
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'sayitqulovabdusalimjon@gmail.com'
# EMAIL_HOST_PASSWORD = '****'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
