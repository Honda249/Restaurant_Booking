from django.shortcuts import render, redirect
from django.forms import BaseModelForm
from django.views.generic import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from base.models import Reservation , Table
from base.forms.reservation_forms import ReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from base.tasks import send_confirmation_email
from django.http import HttpResponse



# Create your views here.

class ReservationCreate(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'base/reservation.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        initial = super().get_initial()
        pk = self.kwargs.get('pk')
        if pk:
            initial['table'] = Table.objects.get(id=pk)
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
       # print(f"Assigning user {self.request.user} to the reservation")
       # return super(ReservationCreate, self).form_valid(form)
        form.save()  # Save the form data
        response = super().form_valid(form)
       # Send confirmation email
        send_confirmation_email.delay(self.request.user.email, self.object.id)
        return response
       # return super().form_valid(form)


class ReservationUpdate(LoginRequiredMixin,UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'base/reservation.html'
    success_url = reverse_lazy('home')  


class ReservationDelete(LoginRequiredMixin,DeleteView):
    model = Reservation
    template_name = 'base/delete-reservation.html'
    success_url = reverse_lazy('home') 

def send_test_email(request):
    send_mail(
        'Test Email',
        'This is a test email.',
        'from@example.com',
        ['honda.muneer@gmail.com'],
    )
    return HttpResponse('Test email sent.')