from django.shortcuts import render
from .models import Transport,Destination,Source
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

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


@login_required
def transports_index(request):
    transports = Transport.objects.get() # I think we need to filter by sorce and destination
    return render(request, 'transports/index.html', {'transports':transports})

@login_required
def transports_detail(request, transport_id):
    transport = Transport.objects.get(id=transport_id)

    return render(request, 'transports/details.html', {
        'transport':transport,
    })