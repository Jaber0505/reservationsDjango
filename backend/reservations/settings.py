from pathlib import Path
from dotenv import load_dotenv
import os

# Chargement des variables d’environnement
load_dotenv()

# Répertoire racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Sécurité
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-replace-this')
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    "reservationsdjango.onrender.com",
    "localhost",
    "127.0.0.1",
]

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'catalogue',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'corsheaders',
    'frontend'
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend' / 'templates'],  # Tu peux personnaliser ce chemin si besoin
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

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'frontend' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

ROOT_URLCONF = 'reservations.urls'
WSGI_APPLICATION = 'reservations.wsgi.application'

# Base de données PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Authentification
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/catalogue/artist'
LOGOUT_REDIRECT_URL = '/'

# Envoi des mails (console pour développement)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalisation
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = 'static/'

# Clé primaire par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ],
}

# Swagger / Spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'Reservation API',
    'DESCRIPTION': 'Documentation de l\'API du projet Reservation',
    'VERSION': '1.0.0',
}

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True