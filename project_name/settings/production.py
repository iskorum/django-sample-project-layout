from .defaults import *

DEBUG = False

ADMINS = [
	# ("Your Name", "your_email@example.com"),
]

MANAGERS = ADMINS

# App used only at production
INSTALLED_APPS += (

)

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',	# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': '{{ project_name }}',
		'USER': '{{ project_name }}',
		'PASSWORD': 'sifreni yaz bura ;)',
		'HOST': 'localhost',
		'PORT': '',
	}
}

ALLOWED_HOSTS = []

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
