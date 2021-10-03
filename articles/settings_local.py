ALLOWED_HOSTS = ['localhost']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_m2m_relations',
        'USER': 'netology_m2m_relations',
        'PASSWORD': 'django',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django.db': {
            'handlers': ['console'],
            'level': DEBUG,
            'propagate': False,
        },
    },
}