import os

DEBUG = True

TESTAPP_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'testsecretkey'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TESTAPP_DIR, 'testdb.sqlite'),
    }
}

STATIC_ROOT = os.path.join(TESTAPP_DIR, '.static')
MEDIA_ROOT = os.path.join(TESTAPP_DIR, '.uploads')

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

ROOT_URLCONF = 'django_generic_flatblocks.tests.testapp.urls'

INSTALLED_APPS = [
    'django_generic_flatblocks',
    'django_generic_flatblocks.tests',
    'django_generic_flatblocks.contrib.gblocks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
]

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

MIDDLEWARE_CLASSES = MIDDLEWARE

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]
