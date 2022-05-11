"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str),
    DJANGO_ALLOWED_HOST=(str, '*'),
    DB_NAME=(str, 'postgres'),
    DB_USER=(str, 'postgres'),
    DB_PWD=(str, 'postgres'),
    DB_HOST=(str, 'db'),
    DB_PORT=(int, 5432),
    CORS_ALLOWED_ORIGINS=(list, []),
    TIME_ZONE=(str, 'Asia/Kathmandu'),
    # Static, Media configs
    DJANGO_STATIC_URL=(str, '/static/'),
    DJANGO_MEDIA_URL=(str, '/media/'),
    DJANGO_STATIC_ROOT=(str, os.path.join(BASE_DIR, "staticfiles")),
    DJANGO_MEDIA_ROOT=(str, os.path.join(BASE_DIR, "media")),
    # Old db
    DB_OLD_NAME=(str, 'idmc'),
    DB_OLD_USER=(str, 'allochi'),
    DB_OLD_PWD=(str, 'postgres'),
    DB_OLD_HOST=(str, 'olddb'),
    DB_OLD_PORT=(int, 5432),
    ENABLE_MIGRATION=(bool, False),
    USE_LOCAL_STORATE=(bool, True),
)

CORS_ALLOWED_ORIGINS = env('CORS_ALLOWED_ORIGINS')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['server', env('DJANGO_ALLOWED_HOST')]

# Local appsexit
LOCAL_APPS = [
    'apps.country',
    'apps.old_gidd',
    'apps.good_practice',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'tinymce',
    'storages',
    'reversion',
] + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PWD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

ENABLE_MIGRATION = env('ENABLE_MIGRATION')
if ENABLE_MIGRATION:
    DATABASES.update({
        'idmc_platform': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_OLD_NAME'),
            'USER': env('DB_OLD_USER'),
            'PASSWORD': env('DB_OLD_PWD'),
            'HOST': env('DB_OLD_HOST'),
            'PORT': env('DB_OLD_PORT'),
            'OPTIONS': {
                'options': '-c search_path=data_platform'
            }
        },
        'idmc_public': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_OLD_NAME'),
            'USER': env('DB_OLD_USER'),
            'PASSWORD': env('DB_OLD_PWD'),
            'HOST': env('DB_OLD_HOST'),
            'PORT': env('DB_OLD_PORT'),
            'OPTIONS': {
                'options': '-c search_path=public'
            }
        }
    })


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

if DEBUG or env('USE_LOCAL_STORATE'):
    STATIC_URL = env('DJANGO_STATIC_URL')
    MEDIA_URL = env('DJANGO_MEDIA_URL')
    STATIC_ROOT = env('DJANGO_STATIC_ROOT')
    MEDIA_ROOT = env('DJANGO_MEDIA_ROOT')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = r'(^/api/.*$)|(^/media/.*$)|(^/graphql/$)'
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'accept-language',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'sentry-trace',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# Tinymce settings
DJANGO_SETTINGS_MODULE = "testtinymce.settings"
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": (
        "advlist autolink lists link image charmap print preview anchor "
        "searchreplace visualblocks code fullscreen insertdatetime media table "
        "paste code help wordcount spellchecker"
    ),
    "toolbar": (
        "undo redo | bold italic underline strikethrough | fontselect "
        "fontsizeselect formatselect | alignleft aligncenter alignright "
        "alignjustify | outdent indent |  numlist bullist checklist | forecolor "
        "backcolor casechange permanentpen formatpainter removeformat | "
        "pagebreak | charmap emoticons | fullscreen  preview save print | "
        "insertfile image media pageembed template link anchor codesample | "
        "a11ycheck ltr rtl | showcomments addcomment code"
    ),
    "custom_undo_redo_levels": 10,
    "language": "en",
}
