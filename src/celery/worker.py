from celery import Celery

from src.config import BACKEND_CONN_URI, BROKER_CONN_URI


worker = Celery('celery', broker=BACKEND_CONN_URI, backend=BROKER_CONN_URI, include=['celery.tasks'])
