from django.db import models
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

class Table(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'Table {self.code}'

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reserv_date = models.DateTimeField("Date Of Reservation")

    def clean(self):
        # Get the time part of the reservation datetime
        reservation_time = self.reserv_date.time()

        # Time validation: reservations must be between 8:00 AM and 11:30 PM
        start_time = timezone.datetime.strptime('08:00', '%H:%M').time()
        end_time = timezone.datetime.strptime('23:30', '%H:%M').time()

        if not (start_time <= reservation_time <= end_time):
            raise ValidationError('Reservations are only allowed between 8:00 AM and 11:30 PM.')

        # Date part of the reservation datetime
        reservation_date = self.reserv_date.date()

        # Duplicate reservation check
        existing_reservations = Reservation.objects.filter(
            user=self.user,
            table=self.table,
        #    reserv_date__date=reservation_date
        ).exclude(pk=self.pk)

        if existing_reservations.exists():
            raise ValidationError('A reservation with the same user and table already exists.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Reservation for {self.user.username} on {self.reserv_date}'


#class Reservation(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  table = models.ForeignKey(Table, on_delete=models.CASCADE)
   # reserv_date = models.DateTimeField("Date Of Reservation")

    #def __str__(self):
     #   return f'Reservation for {self.user.username} on {self.reserv_date}'
