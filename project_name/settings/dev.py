import os
from defaults import PACKAGE_ROOT, INSTALLED_APPS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": "dev.db",
	}
}

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "static", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/static/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ""

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
	os.path.join(PACKAGE_ROOT, "static"),
)


TEMPLATE_DIRS = (
	os.path.join(PACKAGE_ROOT, "templates"),
)

INSTALLED_APPS += (

)


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
