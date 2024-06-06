from django.template.loader import render_to_string
from celery import shared_task
from django.core.mail import send_mail
from .models import Reservation
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_confirmation_email(user_email,user_first_name, reservation_id):
    subject = 'Reservation Confirmation'
    from_email = 'Info@restaurant.com'

    context = {
        'user': {'first_name': user_first_name},
        'reservation_id': reservation_id,
    }
    html_content = render_to_string('confirmation.html', context)

    email = EmailMultiAlternatives(subject, '', from_email, [user_email])
    email.attach_alternative(html_content, "text/html")    
    email.send()

