# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from humidityControl.models import Terrarium


def homepage(request):
    return render(request, 'homepage.html')


class Dashboard(generic.ListView):
    model = Terrarium
    paginate_by = 10


class TerrariumDetailView(generic.DetailView):
    model = Terrarium


class TerrariumListView(generic.ListView):
    model = Terrarium
    paginate_by = 10


class TerrariumCreate(CreateView):
    model = Terrarium
    fields = ['nickname', 'animal', 'climate', 'minHumidity', 'maxHumidity']


class TerrariumUpdate(UpdateView):
    model = Terrarium
    fields = ['nickname', 'animal', 'climate', 'minHumidity', 'maxHumidity']


class TerrariumDelete(DeleteView):
    model = Terrarium
    success_url = reverse_lazy('terrariums')
