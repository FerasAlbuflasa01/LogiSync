from django.shortcuts import render,redirect
from .models import Package
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from django.views.generic import ListView,DetailView

# Create your views here.
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
    return render(request,'home.html')

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

class PackageDelete(DeleteView):
    model =Package
    success_url='/'

