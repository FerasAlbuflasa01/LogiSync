from django.db import models

# Create your models here.
class Package(models.Model):
    code=models.CharField(max_length=15)
    owner=models.CharField(max_length=50)
    desciption=models.TextField(max_length=250)
    price=models.IntegerField()
    wigth=models.FloatField()
    receivedDate=models.DateField()
    
