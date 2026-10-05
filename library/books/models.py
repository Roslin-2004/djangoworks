from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Book(models.Model):
    # id=models.IntegerField()
    title=models.CharField(max_length=20)
    author= models.CharField(max_length=20)
    price= models.IntegerField()
    language= models.CharField(max_length=20)
    pages= models.IntegerField()