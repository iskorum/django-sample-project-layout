from .defaults import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "{{ secret_key }}"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# App used only at development
INSTALLED_APPS += [
]


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = []
