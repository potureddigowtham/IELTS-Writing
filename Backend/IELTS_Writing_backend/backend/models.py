from django.db import models
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField

# Create your models here.


class Acedamic_Writing_Task1(models.Model):
    Title = models.TextField()
    Image = models.ImageField(blank = True)
    Body = models.TextField()
    Description = models.TextField()


class General_Writing_Task1(models.Model):
    Title = models.TextField()
    Image = models.ImageField(blank = True)
    Body = models.TextField()
    Description = models.TextField()


class Academic_General_Writing_Task2(models.Model):
    Title = models.TextField()
    Image = models.ImageField(blank = True)
    Body = models.TextField()
    Description = models.TextField()