# tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_confirmation_email(user_email, reservation_id):
    subject = 'Reservation Confirmation'
    message = f'Your reservation with ID {reservation_id} has been confirmed.'
    from_email = 'webmaster@example.com'
    
    send_mail(subject, message, from_email, [user_email])
