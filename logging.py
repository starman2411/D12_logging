LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console_simple': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
        'console_verbose': {
            'format': '{asctime} {levelname} {pathname} {message}',
            'style': '{',
        },
        'special': {
            'format': '{asctime} {levelname} {pathname} {exc_info} {message}',
            'style': '{',
        },
        'file_simple': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
        'email_format': {
            'format': '{asctime} {levelname} {pathname} {message}',
            'style': '{',
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console_simple',
            'filters': ['require_debug_true'],
        },
        'warning_handler': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'console_verbose',
            'filters': ['require_debug_true'],
        },
        'error_handler': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'special',
            'filters': ['require_debug_true'],
        },
        'general_file_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'file_simple',
            'filters': ['require_debug_false'],
        },
        'errors_file_handler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'special',
            'filters': ['require_debug_true'],
        },
        'security_file_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'email_format',
            'filters': ['require_debug_true'],
        },
        'email_handler': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'file_simple',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        'django': {
            'handlers': ['debug_handler', 'warning_handler', 'error_handler', 'general_file_handler'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['errors_file_handler', 'email_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errors_file_handler', 'email_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors_file_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db_backends': {
            'handlers': ['errors_file_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
