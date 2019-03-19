import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lordandtaylor_site.settings')

app = Celery('lordandtaylor_site', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()