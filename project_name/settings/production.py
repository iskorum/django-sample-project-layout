from .defaults import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ADMINS = [
	# ("Your Name", "your_email@example.com"),
]


ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',	# Add 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': '{{ project_name }}',
		'USER': '{{ project_name }}',
		'PASSWORD': 'sifreni yaz bura ;)',
		'HOST': 'localhost',
		'PORT': '',
	}
}


# App used only at production
INSTALLED_APPS += [
]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY_FILE = os.path.join(BASE_DIR, "production", "secret_key.txt")
with open(SECRET_KEY_FILE) as f:
	SECRET_KEY = f.read().strip()


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
SERVER_EMAIL = 'root@localhost'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
