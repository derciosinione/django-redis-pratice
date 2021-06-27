from django.shortcuts import render
from django.http import JsonResponse

# from django.contrib.auth.models import User
from .models import Friends
from .utils import Red
import time



  # return render(request, 'Web/render.html', {"obj": obj} )

def friends(request):
  start_time = time.time()
  cache_data = Red.get(Friends.__name__)
  if cache_data:
    print('Got from Redis')
    end_time = time.time()
    print(f'{(end_time-start_time):.3f} got: {len(cache_data)} data')
    return JsonResponse(cache_data, safe=False)

  start_time = time.time()
  obj = list(Friends.objects.values())
  print('Got from Postgres')
  end_time = time.time()
  print(f'{(end_time-start_time):.3f} got: {len(cache_data)} data')
  cache_data = Red.set(Friends.__name__, obj)
  return JsonResponse(obj, safe=False)