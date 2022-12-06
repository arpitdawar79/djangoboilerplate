import os

class rest_framework:
    REST_FRAMEWORK = {
          'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
          'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 10)),
          'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
          'DEFAULT_RENDERER_CLASSES': (
              'rest_framework.renderers.JSONRenderer',
              'rest_framework.renderers.BrowsableAPIRenderer',
          ),
          'DEFAULT_PERMISSION_CLASSES': [
              # add custom permissions classes here
          ],

          'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

          'DEFAULT_AUTHENTICATION_CLASSES': (
              'rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication'
          )
      }