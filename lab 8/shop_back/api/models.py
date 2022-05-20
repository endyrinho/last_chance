from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField(max_length=100)
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category': self.category
        }


class Category(models.Model):
    name = models.CharField(max_length=30)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }