from django.shortcuts import render
from django.http import JsonResponse

# from django.contrib.auth.models import User
from .models import Friends
from .utils import Red
import time



  # return render(request, 'Web/render.html', {"obj": obj} )

def friends(request):
  start_time = time.time()

  cache_data = Red.get('api')
  end_time = time.time()
  print(f'{(end_time-start_time):.3f} got: {len(cache_data)} data')

  if cache_data:
    print('Got from Redis')
    return JsonResponse(cache_data, safe=False)

  obj = list(Friends.objects.values())
  print('Got from Postgres')
  cache_data = Red.set("api", obj)
  return JsonResponse(obj, safe=False)