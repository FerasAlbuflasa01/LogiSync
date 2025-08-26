from django.shortcuts import render
from .models import TransportType
from django.views.generic.edit import CreateView

# Create your views here.
class TransportCreate(CreateView):
    model = TransportType
    fields = '__all__'



