from django.views.generic import ListView, CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from base.models import Reservation
from base.forms import ReservationForm

# Create your views here.

class ReservationCreate(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'base/reservation.html'
    success_url = reverse_lazy('home')


class ReservationUpdate(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'base/reservation.html'
    success_url = reverse_lazy('home')  # Redirect after successful form submission

   # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
     #   context['form_type'] = 'Update'
      #  return context

class ReservationDelete(DeleteView):
    model = Reservation
    template_name = 'base/delete-reservation.html'
    success_url = reverse_lazy('home') 