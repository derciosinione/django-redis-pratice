from django.shortcuts import render
from django.http import JsonResponse

# from django.contrib.auth.models import User
from .models import Friends
from .utils import Red
import time


def friends(request):
  cache_data = Red.get('api')
  if cache_data:
    print('Got from Redis')
    return JsonResponse(cache_data, safe=False)


  time.sleep(2)
  obj = list(Friends.objects.values())
  print('Got from Postgres')
  cache_data = Red.set("api", obj)
  return JsonResponse(obj, safe=False)