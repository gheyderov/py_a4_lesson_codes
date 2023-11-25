# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_stories.settings")
app = Celery("food_stories")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# python3 -m celery -A food_stories worker -l info

# celery -A food_stories worker --beat --scheduler django --loglevel=info