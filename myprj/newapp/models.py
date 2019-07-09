from django.db import models

# Create your models here.
class Tableone(models.Model):
    username = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)

