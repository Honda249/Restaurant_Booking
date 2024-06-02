from django.shortcuts import render, redirect
from django.forms import BaseModelForm
from django.views.generic import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from base.models import Reservation
from base.forms.reservation_forms import ReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

class ReservationCreate(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'base/reservation.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
       # print(f"Assigning user {self.request.user} to the reservation")
        form.save()  # Save the form data
       # return super(ReservationCreate, self).form_valid(form)

       # Send confirmation email
        subject = 'Reservation Confirmation'
        message = render_to_string('reservation_confirmation_email.html', {
            'user': self.request.user,
            'reservation': form.instance,
        })
        recipient = self.request.user.email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
        
        return super().form_valid(form)


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