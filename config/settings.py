"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import sys
import environ
from pathlib import Path
from django.utils.translation import gettext_lazy
from config import sentry

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = os.path.join(BASE_DIR, 'apps')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

env = environ.Env(
    PYTEST_XDIST_WORKER=(str, None),
    GIDD_ENVIRONMENT=(str, 'DEVELOPMENT'),  # PROD, STAGING, DEVELOPMENT
    DEBUG=(bool, False),
    SECRET_KEY=str,
    DJANGO_ALLOWED_HOST=(list, ['*']),
    POSTGRES_DB=str,
    POSTGRES_USER=str,
    POSTGRES_PASSWORD=str,
    POSTGRES_HOST=str,
    POSTGRES_PORT=(int, 5432),
    CORS_ALLOWED_ORIGINS=list,
    CSRF_TRUSTED_ORIGINS=list,  # https://gidd-idmc.dev.datafriendlyspace.org
    TIME_ZONE=(str, 'Asia/Kathmandu'),
    APP_DOMAIN=(str, 'http://localhost:7000'),
    # Static, Media configs
    DJANGO_STATIC_URL=(str, '/static/'),
    DJANGO_MEDIA_URL=(str, '/media/'),
    DJANGO_STATIC_ROOT=(str, os.path.join(BASE_DIR, "staticfiles")),
    DJANGO_MEDIA_ROOT=(str, os.path.join(BASE_DIR, "media")),
    # S3 bucket settings
    ENABLE_AWS_BUCKET=(bool, False),
    AWS_S3_ACCESS_KEY_ID=(str, None),
    AWS_S3_SECRET_ACCESS_KEY=(str, None),
    AWS_STORAGE_BUCKET_NAME=(str, ''),
    STATICFILES_LOCATION=(str, 'static'),
    MEDIAFILES_LOCATION=(str, 'media'),
    AWS_STORAGE_BUCKET_NAME_STATIC=(str, 'static'),
    AWS_STORAGE_BUCKET_NAME_MEDIA=(str, 'media'),
    # Sentry
    SENTRY_DSN=(str, None),
    SENTRY_SAMPLE_RATE=(float, 0.2),
    # AWS Translation
    AWS_TRANSLATE_ACCESS_KEY=(str, None),
    AWS_TRANSLATE_SECRET_KEY=(str, None),
    AWS_TRANSLATE_REGION=(str, None),

    DEFAULT_FROM_EMAIL=(str, None),
    USE_AWS_SES=(bool, False),
    # -- If not provided IAM Role will be used
    AWS_SES_REGION_NAME=(str, None),
    AWS_SES_ACCESS_KEY_ID=(str, None),
    AWS_SES_SECRET_ACCESS_KEY=(str, None),
    HCAPTCHA_SITE_KEY=(str, '10000000-ffff-ffff-ffff-000000000001'),
    HCAPTCHA_SECRET=(str, '0x0000000000000000000000000000000000000000'),
)

GIDD_ENVIRONMENT = env('GIDD_ENVIRONMENT')
APP_DOMAIN = env('APP_DOMAIN')

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# See if we are inside a test environment
TESTING = any([
    arg in sys.argv for arg in [
        'test',
        'pytest',
        'py.test',
        '/usr/local/bin/pytest',
        '/usr/local/bin/py.test',
        '/usr/local/lib/python3.6/dist-packages/py/test.py',
    ]
    # Provided by pytest-xdist (If pytest is used)
]) or env('PYTEST_XDIST_WORKER') is not None


ALLOWED_HOSTS = ['server', *env.list('DJANGO_ALLOWED_HOST')]

HCAPTCHA_SECRET = env('HCAPTCHA_SECRET')

# Local appsexit
LOCAL_APPS = [
    'apps.country',
    'apps.old_gidd',
    'apps.good_practice',
    'apps.common',
]

# Application definition

INSTALLED_APPS = [
    # External App (This app has to defined before django.contrib.admin)
    'modeltranslation',  # https://django-modeltranslation.readthedocs.io/en/latest/installation.html#installed-apps

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'strawberry.django',
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
    'django.middleware.locale.LocaleMiddleware',
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
        'DIRS': [os.path.join(APPS_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'config.context_processor.gidd',
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
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

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
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', gettext_lazy('English')),
    ('fr', gettext_lazy('French')),
)
AVAILABLE_LANGUAGES = [lang for lang, _ in LANGUAGES]
MODELTRANSLATION_DEBUG = DEBUG
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('en',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

if env('ENABLE_AWS_BUCKET'):
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = "config.storage_backends.MediaStorage"
    # Use IAM Roles if IAM Credentials aren't provided
    if env('AWS_S3_ACCESS_KEY_ID') and env('AWS_S3_SECRET_ACCESS_KEY'):
        AWS_S3_ACCESS_KEY_ID = env('AWS_S3_ACCESS_KEY_ID')
        AWS_S3_SECRET_ACCESS_KEY = env('AWS_S3_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
    TINYMCE_JS_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/tinymce/tinymce.min.js'
else:
    STATIC_URL = env('DJANGO_STATIC_URL')
    STATIC_ROOT = env('DJANGO_STATIC_ROOT')
    MEDIA_URL = env('DJANGO_MEDIA_URL')
    MEDIA_ROOT = env('DJANGO_MEDIA_ROOT')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

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
# TINYMCE_COMPRESSOR = True

# Sentry Config
SENTRY_DSN = env("SENTRY_DSN")
SENTRY_SAMPLE_RATE = env("SENTRY_SAMPLE_RATE")
SENTRY_ENABLED = False

if SENTRY_DSN:
    SENTRY_CONFIG = {
        "dsn": SENTRY_DSN,
        "send_default_pii": True,
        'release': sentry.fetch_git_sha(BASE_DIR),
        "environment": GIDD_ENVIRONMENT,
        "debug": DEBUG,
        "tags": {
            "site": ",".join(set(ALLOWED_HOSTS)),
        },
    }
    sentry.init_sentry(
        app_type='web',
        **SENTRY_CONFIG,
    )
    SENTRY_ENABLED = True

# AWS Translation
AWS_TRANSLATE_ACCESS_KEY = env('AWS_TRANSLATE_ACCESS_KEY')
AWS_TRANSLATE_SECRET_KEY = env('AWS_TRANSLATE_SECRET_KEY')
AWS_TRANSLATE_REGION = env('AWS_TRANSLATE_REGION')


DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
if env('USE_AWS_SES'):
    EMAIL_BACKEND = 'django_ses.SESBackend'
    AWS_SES_REGION_NAME = env('AWS_SES_REGION_NAME')
    AWS_SES_ACCESS_KEY_ID = env('AWS_SES_ACCESS_KEY_ID')
    AWS_SES_SECRET_ACCESS_KEY = env('AWS_SES_SECRET_ACCESS_KEY')
    AWS_SES_REGION_ENDPOINT = env('AWS_SES_REGION_ENDPOINT')
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

HCAPTCHA_SITE_KEY = env('HCAPTCHA_SITE_KEY')
