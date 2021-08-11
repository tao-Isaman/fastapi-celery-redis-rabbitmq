from celery import Celery

# TODO -> add more connection string
celery = Celery('hello', broker='rabbit', backend='redis')