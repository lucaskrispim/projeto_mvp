from django.db import models
import datetime

# Create your models here.
class User(models.Model):
  name = models.CharField('name',max_length=30)
  password = models.CharField('password',max_length=50)
  phonenumber = models.CharField('phonenumber',max_length=20)
  email = models.CharField('email',max_length=30)

  def __str__(self):
    return f"Name: {self.nome}, Phone Number: {self.phonenumber}, Email: {self.email}, Password: {self.password}"

class Money(models.Model):
  value = models.DecimalField('value', max_digits=6, decimal_places=2,null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Name: {self.user.name}, Money: {self.value}"


# Create your models here.
class Query(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  data = models.DateTimeField('data', default=datetime.datetime.now())

  def __str__(self):
    return f"Name: {self.user.name}, data: {self.data}"

class Adress(models.Model):
  place = models.CharField('place',max_length=30)
  number = models.CharField('number',max_length=10)
  complement = models.CharField('complement',max_length=30)
  city = models.CharField('city',max_length=30)
  uf = models.CharField('uf',max_length=3)
  
  def __str__(self):
    return f"Place: {self.place}, Number: {self.number}, Complement: {self.complement}, City: {self.city}, UF: {self.uf}"

# Create your models here.
class Item(models.Model):
  query = models.ForeignKey(Query, on_delete=models.CASCADE)
  adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
  brand = models.CharField('brand',max_length=20)
  model = models.CharField('model',max_length=20)
  color = models.CharField('color',max_length=20)
  year = models.IntegerField('year')

  def __str__(self):
    return f"Model: {self.model}, Brand: {self.brand}, Color: {self.color}, Year: {self.year}"
