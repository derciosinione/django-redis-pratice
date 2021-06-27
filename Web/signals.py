from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .utils import Redis


@receiver([post_save, post_delete])
def save_friends(sender, instance, **kwargs):
  if sender.__name__!="LogEntry":
    obj = list(sender.objects.values())
    Redis.set(sender.__name__, obj)