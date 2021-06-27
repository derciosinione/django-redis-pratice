from django.shortcuts import render
from django.http import JsonResponse

from .models import Friends
from .utils import Redis

  # return render(request, 'Web/render.html', {"obj": obj} )

def friends_redis(request):
  cache_data = Redis.get(Friends.__name__)
  if cache_data:
    print("Got from Postgres")
    return JsonResponse(cache_data, safe=False)


def friends(request):
  obj = list(Friends.objects.values())
  Redis.set(Friends.__name__, obj)
  print("Got from Postgres")
  return JsonResponse(obj, safe=False)