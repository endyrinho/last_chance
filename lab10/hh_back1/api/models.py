from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    city = models.CharField(max_length=40)
    address = models.TextField(max_length=70)



    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE,default=None)


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company_id': self.company_id
        }
