import os
from .defaults import BASE_DIR, PACKAGE_ROOT


# Number representing the first day of the week.
# The value must be an integer from 0 to 6, where 0 means Sunday, 1 means Monday and so on.
FIRST_DAY_OF_WEEK = 1


# fixtures
FIXTURE_DIRS = (
	os.path.join(BASE_DIR, "fixtures"),
)


# for localization
LOCALE_PATHS = (
	os.path.join(PACKAGE_ROOT, "locale"),
)


# Whether to prepend the "www." subdomain to URLs that don't have it
PREPEND_WWW = False


# If True, the SecurityMiddleware redirects all non-HTTPS requests to HTTPS
# (except for those URLs matching a regular expression listed in SECURE_REDIRECT_EXEMPT)
SECURE_SSL_REDIRECT = False


# -------------------------------------------------------- AUTH -------------------------------------------------------- #
# The URL or named URL pattern where requests are redirected after login when the LoginView doesn’t get a next GET parameter.
LOGIN_REDIRECT_URL = '/accounts/profile/'

# The URL or named URL pattern where requests are redirected for login when using the login_required() decorator, LoginRequiredMixin, or AccessMixin.
LOGIN_URL = '/accounts/login/'

# The number of days a password reset link is valid for. Used by the django.contrib.auth password reset mechanism.
PASSWORD_RESET_TIMEOUT_DAYS = 3
