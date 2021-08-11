import redis

from .worker import celery

# TODO -> redis connection string
#  
redis_store = redis.Redis.from_url('redis')


@celery.task
def move_to_next_stage(name, stage):
    redis_store.set(name, stage)
    return stage