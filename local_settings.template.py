import os

# Cache Config
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_MIDDLEWARE_SECONDS = 60*60

DEBUG = True

if DEBUG:
	EMAIL_PORT = 1025
	CACHE_BACKEND = 'dummy:///'

ADMINS = (
	('Match Strike', 'info@domain.tld'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db.db'        # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/assets/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# E-mail settings.
EMAIL_SUBJECT_PREFIX = '[Match Strike] '
DEFAULT_FROM_EMAIL = 'info@email.tld'

# Social Network Configuration
DELICIOUS_USERS = (('USERNAME','PASSWORD'),)

TWITTER_USERS = ({
	'username':'username',
	'api_key':'XXXXXXXXXXXXXXXXXXXXX',
	'consumer_key':'XXXXXXXXXXXXXXXXXXXXX',
	'consumer_secret':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'oauth_token':'XXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'oauth_secret':'XXXXXXXXXXXXXXXXXXXXX'
},)

# django-compress settings
COMPRESS = True
COMPRESS_VERSION = True
COMPRESS_AUTO = DEBUG # only on dev. use manage.py synccompress on production

# Add the debug toolbar if in debug mode
#if DEBUG == True:
#	MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES+('debug_toolbar.middleware.DebugToolbarMiddleware',)
#	INTERNAL_IPS = ('127.0.0.1',)
#	INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)