__author__ = 'arpitdawar'

import json
import logging
from collections import namedtuple
from re import sub
from threading import local

from django.contrib.auth.models import AnonymousUser

# from .utils import AuthError, jwt_decode_handler, process_token_info

_thread_locals = local()

logger = logging.getLogger()

User = namedtuple(
        'User', [
                    'user_name',
                    'user_permissions',
                    'name',
                    ]
        )


def get_current_user():
    return getattr(_thread_locals, 'user', AnonymousUser())


def set_current_user(user_name):
    setattr(_thread_locals, 'user', user_name)
    return

def get_source_ip_from_request(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_source_ip():
    return getattr(_thread_locals, 'client_ip', '')

def set_source_ip(request):
    client_ip = get_source_ip_from_request(request)
    setattr(_thread_locals, 'client_ip', client_ip)


def set_user_details(user_details):
    setattr(_thread_locals, 'user_details', user_details)
    return

def get_user_details():
    return getattr(_thread_locals, 'user_details')

def set_request_user_permissions(request, parsed_info):
    """[summary]

    Args:
        request (Django Request): Plain old django request object
        parsed_info (Dict): Information extracted from token

    Returns:
    Nothing. This function is called for its side effects.
    """
    user_name = parsed_info.get('user_name')
    user_permissions = parsed_info.get('permissions')
    name = parsed_info.get('name')

    user = User(user_name, user_permissions, name)

    # Set Current User and Attach User to request object
    try:
        set_current_user(
                        user_name=user_name
                    )
        setattr(request, 'user_details', user)
        set_user_details(user)

    except Exception as e:
        logger.error("Unable to attach user in GetCurrentUserMiddleware:", e)
        raise e


class GetCurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            set_current_user(
                user_name=request.user.email
            )

        elif header_token := request.META.get('HTTP_AUTHORIZATION', None):
            # using the new walrus operator here. :-)
            token = sub(
                pattern='Bearer ',
                repl='',
                string=header_token
            )

            # decode the token here to get payload and header
            decoded_data, error = jwt_decode_handler(token)
            if not error:
                # parse decoded decoded data
                parsed_info, error = process_token_info(decoded_data)
                if error:
                    return AuthError(json.dumps({'msg': error}))

            else:
                msg = 'Either the token is invalid or Expired.'
                return AuthError(json.dumps({'msg': msg}))

            # Now we have all the user details,
            # we can proceed to set the current user

            set_request_user_permissions(request, parsed_info)
            set_source_ip(request)

        response = self.get_response(request)

        return response

