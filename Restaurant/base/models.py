from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Table(models.Model):
    code = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.code

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reserv_date = models.DateTimeField("Date Of Reservation")

    def __str__(self):
        return f'Reservation for {self.user.username} on {self.reserv_date}'
