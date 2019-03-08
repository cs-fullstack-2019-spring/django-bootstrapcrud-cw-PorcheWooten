from django.db import models

# Create your models here.

# Each item should include a picture URL, name, description, and price.
class GarageSaleModel(models.Model):
    imageURL = models.CharField(max_length=800, default="")
    name = models.CharField(max_length=200, default="")
    description = models.TextField(max_length=2000)
    price = models.DecimalField(decimal_places=3, max_digits=20)