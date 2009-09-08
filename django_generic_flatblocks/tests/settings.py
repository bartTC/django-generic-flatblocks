from os.path import join, dirname

TEST_DIR = dirname(__file__)

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'
TEST_DATABASE_NAME = ":memory:"

SITE_ID = 1

ROOT_URLCONF = ''

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
#    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django_generic_flatblocks',
    'django_generic_flatblocks.tests',
    'django_generic_flatblocks.contrib.gblocks',
)

TEMPLATE_DIRS = (
    join(TEST_DIR, 'templates'),
)

TEST_RUNNER = 'django-test-coverage.runner.run_tests'