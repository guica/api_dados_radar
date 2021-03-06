from __future__ import absolute_import
# import os
import logging
from celery import Celery, signals
from django.conf import settings


logger = logging.getLogger(__name__)

# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'owl.settings.prod')
app = Celery('api_dados_radares')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@signals.setup_logging.connect
def setup_logging(**kwargs):
    """Setup logging."""
    pass


class RadCeleryException(Exception):
    pass


@app.task(bind=True)
def debug_logging(self):
    logger.error('We just logged something very bad!')
    
@app.task(bind=True)
def debug_exception(self):
    raise RadCeleryException("We are under attack!")
#<<<<<<< Updated upstream
#=======


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )

# @app.task
# def test(arg):
#     print(arg)


# @periodic_task(run_every=timedelta(seconds=10))
# def a():
#     return ' i running periodic task '
#>>>>>>> Stashed changes
