from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView , DetailView
from django.urls import reverse_lazy
from base.models import Table , Reservation

# Create your views here.
class ListView(ListView):
    model = Table
    template_name = 'base/index.html'
    context_object_name = 'tables'


class DetailView(DetailView):
    model = Table
    template_name = 'base/table.html'
    context_object_name = 'table'

class HomePageView(TemplateView):
    template_name = 'base/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tables'] = Table.objects.all()  # Fetch all tables
        context['reservations'] = Reservation.objects.all()  # Fetch all reservations
        return context