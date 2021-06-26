from django.shortcuts import render
from django.http import JsonResponse

# from django.contrib.auth.models import User
from .models import Friends
from .utils import Red



def friends(request):
  obj = list(Friends.objects.values())
  return JsonResponse(obj, safe=False)