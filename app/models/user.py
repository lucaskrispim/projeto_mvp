from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField('name',max_length=30)
  password = models.CharField('password',max_length=50)
  phonenumber = models.CharField('phonenumber',max_length=20)
  email = models.CharField('email',max_length=30)

  def __str__(self):
    return f"Name: {self.name}, Phone Number: {self.phonenumber}, Email: {self.email}, Password: {self.password}"

