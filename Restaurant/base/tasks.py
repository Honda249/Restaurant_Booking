from django.template.loader import render_to_string
from celery import shared_task
from django.core.mail import send_mail
from .models import Reservation
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_confirmation_email(user_email, reservation_id):
    subject = 'Reservation Confirmation'
    message = f'Your reservation with ID {reservation_id} has been confirmed.'

    from_email = 'Info@restaurant.com'
    
    send_mail(subject, message, from_email, [user_email])

