from django.shortcuts import render, redirect
from django.forms import BaseModelForm
from django.views.generic import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from base.models import Reservation
from base.forms.reservation_forms import ReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


# Create your views here.

class ReservationCreate(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'base/reservation.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
       # form.instance.user = self.request.user
        print(f"Assigning user {self.request.user} to the reservation")
        form.save()  # Save the form data
        return super().form_valid(form)
       # return super(ReservationCreate, self).form_valid(form)


class ReservationUpdate(LoginRequiredMixin,UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'base/reservation.html'
    success_url = reverse_lazy('home')  # Redirect after successful form submission

   # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
     #   context['form_type'] = 'Update'
      #  return context

class ReservationDelete(LoginRequiredMixin,DeleteView):
    model = Reservation
    template_name = 'base/delete-reservation.html'
    success_url = reverse_lazy('home') 