import redis
import json

rds = redis.StrictRedis(port=6379, db=0)

class Red:
  def set(cache_key, data):
    data = json.dumps(data)
    rds.set(cache_key, data)

  def get(cache_key):
    pass

