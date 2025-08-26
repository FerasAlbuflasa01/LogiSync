from django.shortcuts import render
from .models import TransportType
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class TransportTypeCreate(CreateView):
    model = TransportType
    fields = '__all__'

class TransportTypeUpdate(UpdateView):
    model = TransportType
    fields = 'code'

class TransportTypeDelete(DeleteView):
    model = TransportType
    succes_url = '/transports/'



