from datetime import timedelta
from django.core.exceptions import ImproperlyConfigured
import os


class simple_jwt:
    if JWT_SIGNING_KEY_PATH := os.getenv('TOKEN_SIGNING_KEY_PATH'):
        with open(JWT_SIGNING_KEY_PATH, 'rb') as f:
            JWT_SIGNING_SECRET = f.read()
            if not JWT_SIGNING_SECRET:
                raise ImproperlyConfigured(
                    "Signing Key File should not be empty")
    else:
        raise ImproperlyConfigured("TOKEN_SIGNING_KEY_PATH is not set")

    if JWT_VERIFICATION_KEY_PATH := os.getenv('TOKEN_VERIFICATION_KEY_PATH'):
        with open(JWT_VERIFICATION_KEY_PATH, 'rb') as f:
            JWT_VERIFICATION_SECRET = f.read()
            if not JWT_VERIFICATION_SECRET:
                raise ImproperlyConfigured(
                    "Verification Key File should not be empty")
    else:
        raise ImproperlyConfigured("TOKEN_VERIFICATION_KEY_PATH is not set")

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        'ROTATE_REFRESH_TOKENS': True,
        'BLACKLIST_AFTER_ROTATION': False,
        'UPDATE_LAST_LOGIN': True,
        'ALGORITHM': 'RS256',
        'SIGNING_KEY': JWT_SIGNING_SECRET,
        'VERIFYING_KEY': JWT_VERIFICATION_SECRET,
    }
