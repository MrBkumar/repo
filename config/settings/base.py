"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import sys
from os import path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("core")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "l+r0b4%#_&*75*%*kfk5w4epc$ms9aeikk2wzn2uaep(d!r_m8"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "widget_tweaks",
    "crispy_forms",
]
LOCAL_APPS = [
    "config",
    "core.customadmin.apps.CustomadminConfig",
    "core.customer.apps.CustomerConfig",
    "core.delivery_agent.apps.DeliveryAgentConfig",
    "core.store_manager.apps.StoreManagerConfig",
    "core.user.apps.UserConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    # "config.middleware.exception_middleware.ExceptionMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            path.join(APPS_DIR, "customadmin", "templates", "customadmin"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.customadmin.context_processors.settings_context",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "quickly_grocery_app",
        "USER": "postgres",
        "HOST": "localhost",
        "PASSWORD": "bkumar",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Rest Framework config
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": ("rest_framework.pagination.LimitOffsetPagination"),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "SEARCH_PARAM": "q",
}

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

AUTH_USER_MODEL = "user.User"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_ROOT = path.join(APPS_DIR, "media").replace("\\", "/")

MEDIA_URL = "/media/"

CRISPY_TEMPLATE_PACK = "bootstrap4"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = path.join(APPS_DIR, "customadmin", "static", "customadmin").replace(
    "\\", "/"
)

STATIC_URL = "/static/"

STATICFILES_DIRS = (path.join(APPS_DIR, "customadmin", "static"),)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

LOGIN_URL = "customadmin:auth_login"

LOGOUT_REDIRECT_URL = "customadmin:auth_login"
LOGIN_REDIRECT_URL = "customadmin:index"

SITE_ID = 1

# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
# EMAIL_TIMEOUT = 5
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Used in customadmin.context_processors.common
PROJECT_TITLE = "Quickly eCommerce"  # &trade;
COPYRIGHT = "Quickly eCommerce"


ADMIN_HIDE_PERMS = [
    "contenttypes",
    "sessions",
    "admin",
    "authtoken",
    "thumbnail",
    "corsheaders",
    "authtoken",
    "sites",
    "account",
    "socialaccount",
    "django_celery_beat",
]

SUPER_USER = {
    "ADMIN_EMAIL": os.getenv("ADMIN_EMAIL"),
    "ADMIN_USERNAME": os.getenv("ADMIN_USERNAME"),
    "ADMIN_PASSWORD": os.getenv("ADMIN_PASSWORD"),
}
