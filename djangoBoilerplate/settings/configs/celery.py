
class celery:
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'

    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
    CELERY_ACCEPT_CONTENT = ["json"]
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
    CELERY_TASK_SERIALIZER = "json"
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler
    CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
    CELERY_IGNORE_RESULT = True

    CELERY_TASK_ALWAYS_EAGER = False
