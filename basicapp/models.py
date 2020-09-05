from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=60)
    age = models.PositiveIntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    email = models.CharField(max_length=60)
    ph_no = models.PositiveIntegerField()