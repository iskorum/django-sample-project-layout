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

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ""

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