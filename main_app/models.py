from django.db import models

# Create your models here.
class Finch(models.Model):
  breed = models.CharField(max_length=100)
  habitat = models.CharField(max_length=100)
  food = models.CharField(max_length=100)

def __str__(self):
  return self.breed