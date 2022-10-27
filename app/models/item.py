from django.db import models
from .query import Query
from .address import Address

# Create your models here.
class Item(models.Model):
  query = models.ForeignKey(Query, on_delete=models.CASCADE)
  address = models.ForeignKey(Address, on_delete=models.CASCADE)
  brand = models.CharField('brand',max_length=20)
  model = models.CharField('model',max_length=20)
  color = models.CharField('color',max_length=20)
  year = models.IntegerField('year')

  def __str__(self):
    return f"Model: {self.model}, Brand: {self.brand}, Color: {self.color}, Year: {self.year}"