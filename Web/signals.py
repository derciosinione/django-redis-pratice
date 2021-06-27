from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Friends


@receiver(post_save, sender=Friends)
def create_friends(sender, instance, created, **kwargs):
  if created:
    print("Created")
    print(created)
    print(instance)



@receiver(post_save)
def save_friends(sender, instance, **kwargs):
  if sender.__name__=="LogEntry":
    pass
  else:
    print(sender.__name__)