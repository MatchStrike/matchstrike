# Django settings for matchstrike project.
import os

# Location of project directory.
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'assets')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
	#'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	os.path.join(SITE_ROOT, 'templates'),
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'django_extensions',
	'compress',
	'syncr.twitter',
	'syncr.delicious',
	'tagging',
	'contact',
	'social',
	'gunicorn',
	'sentry.client'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"context_processors.default",
)

COMPRESS_CSS = {
	'main': {
		'source_filenames': ('css/matchstrike.css',),
		'output_filename': 'css/matchstrike.r?.css',
    },
	'ie7': {
		'source_filenames': ('css/ie7.css',),
		'output_filename': 'css/ie7.r?.css',
    },
	'ie6': {
		'source_filenames': ('css/ie6.css',),
		'output_filename': 'css/ie6.r?.css',
    },
}

COMPRESS_JS = {
	'main': {
		'source_filenames': (
			'js/jquery.js',
			'js/jquery.tools.min.js',
			'js/jquery.cycle.min.js',
			'js/googleAnalytics.js',
			'js/matchstrike.js',
			),
		'output_filename': 'js/matchstrike.r?.js',
	},
	'ie7': {
		'source_filenames': (
			'js/ie7.js',),
		'output_filename': 'js/ie7.r?.js',
	},
	'ie6': {
		'source_filenames': (
			'js/supersleight.plugin.js',
			'js/ie6.js',),
		'output_filename': 'js/ie6.r?.js',
	},
}

# Import local settings.
try:
    from local_settings import *
except ImportError:
    pass
