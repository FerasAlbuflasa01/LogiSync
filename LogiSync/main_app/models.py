from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


# Create your models here.
    
class Container(models.Model):
    tracking_location = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    weight_capacity = models.FloatField()
    currnt_weight_capacity = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('container_detail', kwargs={'container_id': self.id})
    
    def __str__(self):
        return f"Container {self.id} - {self.tracking_location}"

class Package(models.Model):
    code=models.CharField(max_length=20)
    owner=models.CharField(max_length=50)
    description=models.TextField(max_length=250)
    price=models.IntegerField()
    weight=models.FloatField()
    receivedDate=models.DateField()
    container = models.ForeignKey(Container, on_delete=models.SET_NULL, null=True, blank=True)
    inContainer=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.code
    def get_absolute_url(self):
        return reverse('packages_detail', kwargs={'pk': self.id})  

class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # CODE = models.CharField(max_length=20)

class Source(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # CODE = models.CharField(max_length=20)

class Transport(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    description = models.TextField(max_length=250)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    # CODE = models.CharField(max_length=20)    

class TransportType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')

    def get_absolute_url(self):
        return reverse("detail", kwargs={'transport_id': self.id})
    
    def __str__(self):
        return self.name
