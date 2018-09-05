from .defaults import *

DEBUG = False

ADMINS = [
	# ("Your Name", "your_email@example.com"),
]

MANAGERS = ADMINS

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
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


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY_FILE = os.path.join(BASE_DIR, "production", "secret_key.txt")
with open(SECRET_KEY_FILE) as f:
	SECRET_KEY = f.read().strip()

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "static")


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
SERVER_EMAIL = 'root@localhost'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
