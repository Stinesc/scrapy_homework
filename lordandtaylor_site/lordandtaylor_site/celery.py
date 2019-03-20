import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lordandtaylor_site.settings')

app = Celery('lordandtaylor_site', backend='redis://localhost:6379/1', broker='redis://localhost:6379/1')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()