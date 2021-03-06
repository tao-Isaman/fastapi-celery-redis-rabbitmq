import os

import os

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_CELERY_DB_INDEX = os.environ.get('REDIS_CELERY_DB_INDEX')
REDIS_STORE_DB_INDEX = os.environ.get('REDIS_STORE_DB_INDEX')

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

BROKER_CONN_URI = f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}"
BACKEND_CONN_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB_INDEX}"
REDIS_STORE_CONN_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_STORE_DB_INDEX}"

stages = ["confirmed", "shipped", "in transit", "arrived", "delivered"]
STAGING_TIME = 15 # seconds