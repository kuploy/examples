import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-not-for-production")
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
ALLOWED_HOSTS = ["*"]  # served behind the Kuploy ingress

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
]
MIDDLEWARE = ["django.contrib.sessions.middleware.SessionMiddleware"]
ROOT_URLCONF = "mysite.urls"
WSGI_APPLICATION = "mysite.wsgi.application"

# DATABASE_URL is injected by the stack connection (db.connectionString).
DATABASES = {"default": dj_database_url.parse(os.environ["DATABASE_URL"])}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
