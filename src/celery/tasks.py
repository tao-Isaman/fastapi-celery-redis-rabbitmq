import redis

from src.celery.worker import worker

from src.config import REDIS_STORE_CONN_URI

redis_store = redis.Redis.from_url(REDIS_STORE_CONN_URI)


@worker.task
def move_to_next_stage(name, stage):
    redis_store.set(name, stage)
    return stage