from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=64)
    Description = models.CharField(max_length=200)