from django.db import models
from django.urls import reverse

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # CODE = models.CharField(max_length=20)

class Source(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # CODE = models.CharField(max_length=20)

class Transport(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    description = models.TextField(max_length=250)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    # CODE = models.CharField(max_length=20)    


    def get_absolute_url(self):
        return reverse("detail", kwargs={'transport_id': self.id})
    
    def __str__(self):
        return self.name




