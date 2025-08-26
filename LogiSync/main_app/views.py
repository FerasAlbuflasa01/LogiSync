from django.shortcuts import render
from .models import TransportType
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class TransportCreate(CreateView):
    model = TransportType
    fields = '__all__'

class TransportUpdate(UpdateView):
    models = TransportType
    fields = code



