from django.db import models
from .user import User

# Create your models here.
class Money(models.Model):
  value = models.DecimalField('value', max_digits=6, decimal_places=2,null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Name: {self.user.name}, Money: {self.value}"


