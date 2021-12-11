import os

from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptowatch.settings')

app = Celery('cryptowatch')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')


# Load task modules from all registered Django apps.
app.conf.beat_schedule = {
    'update_task': {
        'task': 'cryptoapp.tasks.get_crypto_data',
        'schedule': crontab(minute="*"),
#'schedule': crontab(hour=0, minute=46, day_of_month=19, month_of_year = 6),
        # 'args': (2,)
    }


}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')