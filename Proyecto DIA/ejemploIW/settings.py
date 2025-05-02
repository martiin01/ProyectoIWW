import os
from pathlib import Path

# ─── Rutas ────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── Seguridad básica ─────────────────────────────────────────────────────
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-xxxx")
DEBUG      = True
ALLOWED_HOSTS = []

# ─── Aplicaciones ─────────────────────────────────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Terceros
    "corsheaders",
    "rest_framework",
    "drf_spectacular",

    # Tuyas
    "user",
    "producto",
    "categoria",
    "cupon",
    "sede",
]

# ─── Middleware ligero ────────────────────────────────────────────────────
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",            # CORS
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "ejemploIW.urls"

# ─── Templates ────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND":  "django.template.backends.django.DjangoTemplates",
        "DIRS":     [],            # deja vacío o pon tu carpeta de plantillas
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ejemploIW.wsgi.application"

# ─── Base de datos simple ─────────────────────────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":   BASE_DIR / "db.sqlite3",
    }
}

# ─── Django REST Framework ────────────────────────────────────────────────
REST_FRAMEWORK = {
    # Usamos drf-spectacular para el esquema OpenAPI
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # Autenticación y permisos básicos
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# ─── drf-spectacular ────────────────────────────────────────────────────
SPECTACULAR_SETTINGS = {
    "TITLE":       "IW – React + Django API",
    "DESCRIPTION": "API para IW",
    "VERSION":     "1.0.0"
}

# ─── Internacionalización ──────────────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE     = "UTC"
USE_I18N      = True
USE_TZ        = True

# ─── Archivos estáticos ─────────────────────────────────────────────────
STATIC_URL = "/static/"

# ─── User personalizado si lo usas ──────────────────────────────────────
AUTH_USER_MODEL = "user.User"

# ─── Auto field ─────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ─── CORS ────────────────────────────────────────────────────────────────
CORS_ALLOW_ALL_ORIGINS = True
