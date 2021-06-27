from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
import django.utils.timezone


class Users(AbstractUser):
    # id = models.CharField(max_length=50, primary_key=True, default=uuid4, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=254, unique=True, blank=False, verbose_name="email address")

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"
    REQUIRED_FIELDS = ('email',)

    def __str__(self):
        return self.username

    class Meta:
        # # managed = False
        db_table = 'users'
        ordering = ('-date_joined', 'username',)


class Friends(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, db_index=True, blank=False)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True)
    creation_date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name