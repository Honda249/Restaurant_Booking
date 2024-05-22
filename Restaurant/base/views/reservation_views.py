from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from base.models import Reservation
from base.forms import ReservationForm

# Create your views here.

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'base/reservation.html'
    success_url = reverse_lazy('home')