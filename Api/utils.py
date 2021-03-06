import redis
import json
from django.core.serializers.json import DjangoJSONEncoder

rds = redis.StrictRedis(host='localhost', port=6379, db=0)

class Redis:
  def set(cache_key, data):
    data = json.dumps(data, cls=DjangoJSONEncoder)
    rds.set(cache_key, data)
    return True

  def get(cache_key):
    cache_data = rds.get(cache_key)
    if not cache_data:
      return None
    cache_data = json.loads(cache_data)
    return cache_data