from .defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = [
	# ("Your Name", "your_email@example.com"),
]

MANAGERS = ADMINS

# App used only at development
INSTALLED_APPS += (

)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "static", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/static/media/"

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
