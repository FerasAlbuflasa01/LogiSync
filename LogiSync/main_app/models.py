from django.db import models
from django.urls import reverse

# Create your models here.
class Package(models.Model):
    code=models.CharField(max_length=20)
    owner=models.CharField(max_length=50)
    description=models.TextField(max_length=250)
    price=models.IntegerField()
    weight=models.FloatField()
    receivedDate=models.DateField()

    def __str__(self):
        return self.code
    def get_absolute_url(self):
        return reverse('package_detail', kwargs={'pk': self.id})
