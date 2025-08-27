

from django.shortcuts import render,redirect
from .models import Package,Transport,Destination,Source, TransportType, Container
from django.views.generic.edit import CreateView,UpdateView,DeleteView 
from django.views.generic import ListView,DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

# Create your views here.

# home / about 
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')




#Containers
class ContainerCreate(LoginRequiredMixin, CreateView):
    model = Container
    fields = ['container_id', 'tracking_location', 'description', 'weight' ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ContainerUpdate(LoginRequiredMixin, UpdateView):
    model = Container
    fields = [ 'tracking_location', 'description', 'weight',]
    def get_queryset(self):
        return Container.objects.filter(user=self.request.user)

class ContainerDelete(LoginRequiredMixin, DeleteView):
    model = Container
    success_url = '/'
    
class ContainerDetail(LoginRequiredMixin, DetailView):
    model = Container
    
class ContainerList(LoginRequiredMixin, ListView):
    model = Container
    def get_queryset(self):
        return Container.objects.filter(user=self.request.user)




# package
class PackageList(LoginRequiredMixin, ListView):
    model=Package
    def get_queryset(self):
        return Package.objects.filter(user=self.request.user)

class PackageDetails(LoginRequiredMixin, DetailView):
    model=Package

@login_required
def package_create(request):
    for package in listOfPackags:
        # if(not Package.objects.get(code=package['code'])):
        newPackage = Package(
                code=package['code'],
                owner=package['owner'],
                description=package['description'],
                price=package['price'],
                weight=package['weight'],
                receivedDate=package['receivedDate'],
                user=request.user
            )
        newPackage.save()
    return redirect('home')

class PackageUpdate(LoginRequiredMixin, UpdateView):
    model=Package
    fields = ['description','price','weight']

class PackageDelete(LoginRequiredMixin, DeleteView):
    model =Package
    success_url='/'




################## TRANSPORT TYPE ######################

class TransportList(LoginRequiredMixin,ListView):
    model = Transport
    
    def get_queryset(self):
        return Transport.objects.filter(user=self.request.user)

class TransportDetails(LoginRequiredMixin,DetailView):
    model = Transport
    fields = '__all__'
    
class TransportTypeCreate(LoginRequiredMixin, CreateView):
    model = TransportType
    fields = '__all__'

class TransportTypeUpdate(LoginRequiredMixin, UpdateView):
    model = TransportType
    fields = ['code']

class TransportTypeDelete(LoginRequiredMixin, DeleteView):
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



def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)