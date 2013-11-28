import os
from .defaults import BASE_DIR, PACKAGE_ROOT

# Whether to use HttpOnly flag on the CSRF cookie.
# If this is set to True, client-side JavaScript will not to be able to access the CSRF cookie.
CSRF_COOKIE_HTTPONLY = False

# The name of the cookie to use for the CSRF authentication token.
# This can be whatever you want.
CSRF_COOKIE_NAME = 'csrftoken'

# Number representing the first day of the week.
# The value must be an integer from 0 to 6, where 0 means Sunday, 1 means Monday and so on.
FIRST_DAY_OF_WEEK = 1

# fixtures
FIXTURE_DIRS = (
	os.path.join(BASE_DIR, "fixtures"),
)

# TODO: check if this setting is necassary
# # for localization
# LOCALE_PATHS = (
# 	os.path.join(PACKAGE_ROOT, "locale"),
# )

# Whether to prepend the "www." subdomain to URLs that don't have it
PREPEND_WWW = False


TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.core.context_processors.tz",
	"django.core.context_processors.request",
	"django.contrib.messages.context_processors.messages",
)


# -------------------------------------------------------- AUTH -------------------------------------------------------- #
# The URL where requests are redirected after login when the contrib.auth.login view gets no next parameter.
# This is used by the login_required() decorator, for example.
LOGIN_REDIRECT_URL = '/accounts/profile/'

#The URL where requests are redirected for login, especially when using the login_required() decorator.
LOGIN_URL = '/accounts/login/'

# The number of days a password reset link is valid for. Used by the django.contrib.auth password reset mechanism.
PASSWORD_RESET_TIMEOUT_DAYS = 3
