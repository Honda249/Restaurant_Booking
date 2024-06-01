from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView , DetailView
from django.urls import reverse_lazy
from base.models import Table , Reservation
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'base/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tables'] = Table.objects.all()  # Fetch all tables
        
        if self.request.user.is_authenticated:
            context['reservations'] = Reservation.objects.filter(user=self.request.user)  # Fetch user reservations
        else:
            context['reservations'] = Reservation.objects.none()  # Empty queryset for anonymous users

        return context

class ListView(LoginRequiredMixin,ListView):
    model = Table
    template_name = 'base/index.html'
    context_object_name = 'tables'


class DetailView(LoginRequiredMixin,DetailView):
    model = Table
    template_name = 'base/table.html'
    context_object_name = 'table'
