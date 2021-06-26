from django.shortcuts import render
from django.http import JsonResponse
from .models import Friends
from django.contrib.auth.models import User


def friends(request):
  obj = list(Friends.objects.values())
  return JsonResponse(obj, safe=False)