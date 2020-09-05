from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# For model query set practice Company , Language, Programmer

class Company(models.Model):
    name = models.CharField(max_length=54)
    location = models.CharField(max_length=54)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=54)
    creator = models.CharField(max_length=54)
    paradigm = models.CharField(max_length=54)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=54)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name

