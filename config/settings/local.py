from .base import *

# cors headers
INSTALLED_APPS += ['corsheaders',]
MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware',]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'sampledb'),
        'USER': os.environ.get('DJANGO_DB_USERNAME', 'sampleuser'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'samplesecret'),

        # if not use docker container as django server
        # 'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),

        'HOST': os.environ.get('DJANGO_DB_HOST', 'basic-db'),

        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}