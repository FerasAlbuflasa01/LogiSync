from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Container(models.Model):
    container_id = models.CharField(max_length=50, primary_key=True)
    tracking_location = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    weight = models.CharField(max_length=10)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('container_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f"Container {self.container_id} - {self.tracking_location}"