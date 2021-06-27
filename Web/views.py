from django.shortcuts import render
from django.http import JsonResponse

from .models import Friends
from .utils import Redis

  # return render(request, 'Web/render.html', {"obj": obj} )

def friends_redis(request):
  cache_data = Redis.get(Friends.__name__)
  if cache_data:
    # return JsonResponse(cache_data, safe=False)
    return render(request, 'Web/render.html', {"obj": cache_data} )



def friends(request):
  obj = list(Friends.objects.values())
  Redis.set(Friends.__name__, obj)
  return render(request, 'Web/render.html', {"obj": obj} )
  # return JsonResponse(obj, safe=False)