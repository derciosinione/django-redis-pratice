from django.shortcuts import render
from django.http import JsonResponse

from .models import Friends
from .utils import Redis
from django.db.models.functions import Cast
from django.db.models import CharField, TextField
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
  # return render(request, 'Web/render.html', {"obj": obj} )
  # return JsonResponse(obj, safe=False)

def friends_redis(request):
  cache_data = Redis.get(Friends.__name__)
  if cache_data:
    return render(request, 'Api/render.html', {"obj": cache_data})
  return render(request, 'Api/render.html', {"obj": cache_data})


def friends(request):
  obj = list(Friends.objects.values())
  my = json.dumps(obj, indent=1, cls=DjangoJSONEncoder)
  print(my)
  # Redis.set(Friends.__name__, obj)
  return render(request, 'Api/render.html', {"obj": obj})
