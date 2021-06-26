from django.db import models


class Friends(models.Model):
  name = models.CharField(max_length=100, db_index=True, blank=False)
  age = models.IntegerField(null=True)
  email = models.EmailField(max_length=100, null=True)

  def __str__(self):
    return self.name