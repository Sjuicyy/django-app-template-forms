from unicodedata import name
from django.db import models

# Create your models here.
class student(models.Model):
    name          = models.CharField(max_length=50)
    subject       = models.CharField(max_length=50)
    roll_num      = models.FloatField()
    class_teacher = models.CharField(max_length=50)
  