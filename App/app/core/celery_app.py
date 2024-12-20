# Configura Celery 
from celery import Celery
from app.core.config import settings

celery_app = Celery("worker", broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)

celery_app.conf.task_routes = {"app.tasks.*": "main-queue"}
celery_app.conf.timezone = "UTC"