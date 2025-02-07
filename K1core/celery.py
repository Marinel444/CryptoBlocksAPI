import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "K1core.settings")

app = Celery("K1core")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "fetch_blocks_every_minute": {
        "task": "blocks.tasks.fetch_and_store_blocks",
        "schedule": crontab(minute="*"),
    },
}
