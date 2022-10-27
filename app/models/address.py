from django.db import models

class Address(models.Model):
  place = models.CharField('place',max_length=30)
  number = models.CharField('number',max_length=10)
  complement = models.CharField('complement',max_length=30)
  city = models.CharField('city',max_length=30)
  uf = models.CharField('uf',max_length=3)
  
  def __str__(self):
    return f"Place: {self.place}, Number: {self.number}, Complement: {self.complement}, City: {self.city}, UF: {self.uf}"
