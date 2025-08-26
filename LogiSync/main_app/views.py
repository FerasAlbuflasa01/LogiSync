from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Container

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class ContainerCreate(CreateView):
    model = Container
    fields = ['container_id', 'tracking_location', 'description', 'weight' ]
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ContainerUpdate(UpdateView):
    model = Container
    fields = [ 'tracking_location', 'description', 'weight',]
    
class ContainerDelete(DeleteView):
    model = Container
    success_url = 'home'
    
class ContainerDetail(DetailView):
    model = Container
    
class ContainerList(ListView):
    model = Container

    