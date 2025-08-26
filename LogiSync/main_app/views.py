

from django.shortcuts import render,redirect
from .models import Package,Transport,Destination,Source, TransportType, Container
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TransportList(LoginRequiredMixin,ListView):
    model = Transport

class TransportDetails(LoginRequiredMixin,DetailView):
    model = Transport
    fields = '__all__'

listOfPackags = [
    {
        "code": "ITEM001",
        "owner": "Alice Johnson",
        "description": "A high-quality leather wallet.",
        "price": 50,
        "weight": 0.2,
        "receivedDate": "2023-08-01"
    },
    {
        "code": "ITEM002",
        "owner": "Bob Smith",
        "description": "Durable running shoes.",
        "price": 75,
        "weight": 1.0,
        "receivedDate": "2023-08-05"
    },
    {
        "code": "ITEM003",
        "owner": "Charlie Brown",
        "description": "Wireless Bluetooth headphones.",
        "price": 100,
        "weight": 0.3,
        "receivedDate": "2023-08-10"
    },
    {
        "code": "ITEM004",
        "owner": "Diana Prince",
        "description": "Smartwatch with health tracking.",
        "price": 150,
        "weight": 0.5,
        "receivedDate": "2023-08-15"
    },
    {
        "code": "ITEM005",
        "owner": "Ethan Hunt",
        "description": "Portable charger for devices.",
        "price": 30,
        "weight": 0.4,
        "receivedDate": "2023-08-20"
    }
]

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
    success_url = '/'
    
class ContainerDetail(DetailView):
    model = Container
    
class ContainerList(ListView):
    model = Container

# package
class PackageList(ListView):
    model=Package

class PackageDetails(DetailView):
    model=Package

def package_create(request):
    for package in listOfPackags:
        # if(not Package.objects.get(code=package['code'])):
        newPackage = Package(
                code=package['code'],
                owner=package['owner'],
                description=package['description'],
                price=package['price'],
                weight=package['weight'],
                receivedDate=package['receivedDate']
            )
        newPackage.save()

    return redirect('home')

class PackageUpdate(UpdateView):
    model=Package
    fields = ['description','price','weight']

class PackageDelete(DeleteView):
    model =Package
    success_url='/'
 
################## TRANSPORT TYPE ######################

class TransportTypeCreate(CreateView):
    model = TransportType
    fields = '__all__'

class TransportTypeUpdate(UpdateView):
    model = TransportType
    fields = 'code'

class TransportTypeDelete(DeleteView):
    model = TransportType
    succes_url = '/transports/'
    
#################### TRANSPORT  ###########################

class TransportCreate(LoginRequiredMixin,CreateView):
    model = Transport
    fields = ['name','capacity','image','description','destination','source']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TransportUpdate(LoginRequiredMixin,UpdateView):
    model = Transport
    fields = ['capacity','description','destination','source']


class TransportDelete(LoginRequiredMixin,DeleteView):
    model = Transport
    success_url = '/transports/'


# @login_required
# def transports_index(request):
#     transports = Transport.objects.get() # I think we need to filter by sorce and destination
#     return render(request, 'transports/index.html', {'transports':transports})

# @login_required
# def transports_detail(request, transport_id):
#     transport = Transport.objects.get(id=transport_id)
#     return render(request, 'transports/details.html', {
#         'transport':transport,
#     })
