from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=254, unique=True, blank=False, verbose_name="email address")
    image = models.ImageField(default='default.jpg', upload_to='Users', null=True, blank=True)
    tin = models.CharField(unique=True, max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    account_state = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_code = models.CharField(max_length=50, blank=True, null=True)

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
    creation_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name