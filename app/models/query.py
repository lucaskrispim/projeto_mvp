from django.db import models
from .user import User
import datetime

# Create your models here.
class Query(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  data = models.DateTimeField('data', default=datetime.datetime.now())

  def __str__(self):
    return f"Name: {self.user.name}, data: {self.data}"