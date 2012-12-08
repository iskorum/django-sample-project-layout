import os
from defaults import PACKAGE_ROOT, INSTALLED_APPS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',	# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': '{{ project_name }}',			# Or path to database file if using sqlite3.
		'USER': 'root',							# Not used with sqlite3.
		'PASSWORD': 'root',						# Not used with sqlite3.
		'HOST': 'localhost',					# Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',								# Set to empty string for default. Not used with sqlite3.
	}
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "tr-TR"

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False


STATICFILES_DIRS = (
	
)

INSTALLED_APPS += (

)


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"