from django.shortcuts import render
from django.http import JsonResponse

# from django.contrib.auth.models import User
from .models import Friends
from .utils import Red
import time


def friends(request):
  cache_data = Red.get('api')
  if cache_data:
    return cache_data
  
  time.sleep(2)
  obj = list(Friends.objects.values())
  cache_data = Red.set("api", obj)
  return JsonResponse(obj, safe=False)