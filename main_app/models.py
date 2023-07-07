from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
  breed = models.CharField(max_length=100)
  habitat = models.CharField(max_length=100)
  food = models.CharField(max_length=100)

def __str__(self):
  return f'{self.breed} ({self.id})'

def get_absolute_url(self):
  return reverse('detail', kwargs={'finch_id': self.id})