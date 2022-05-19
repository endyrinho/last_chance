from django.db import models

# Create your models here.

class Companies(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    city = models.CharField(max_length=40)
    address = models.TextField(max_length=70)

class Vacancies(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    salary = models.FloatField
    company = models.ForeignKey
