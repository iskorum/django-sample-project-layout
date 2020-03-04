from .dev import *

SECRET_KEY = ""

INSTALLED_APPS += [
	'debug_toolbar'
]

MIDDLEWARE = [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

INTERNAL_IPS = [
    '127.0.0.1',
]

EMAIL_BACKEND = ""
SERVER_EMAIL = ''

EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
