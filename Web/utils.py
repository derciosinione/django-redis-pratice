import redis

rd = redis.StrictRedis(port=6379, db=0)

class Red:
  def set(cache_key, data):
    pass

  def get(cache_key):
    pass

