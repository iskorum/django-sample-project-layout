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


INSTALLED_APPS += (

)


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
