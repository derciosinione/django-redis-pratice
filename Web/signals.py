from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Friends
from .utils import Red


@receiver(post_save, sender=Friends)
def create_friends(sender, instance, created, **kwargs):
  if created:
    print(instance)



@receiver([post_save, post_delete])
def save_friends(sender, instance, **kwargs):
  if sender.__name__!="LogEntry":
    obj = sender.objects.values()
    cache_data = Red.set(sender.__name__, obj)
    print(cache_data)