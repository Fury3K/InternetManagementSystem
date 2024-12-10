# In models.py
from django.db import models

class Reservations(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('cancelled', 'Cancelled'),
    ]

    reservationID = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')
    adminID = models.ForeignKey('admin_app.Admin', on_delete=models.CASCADE, null=True, blank=True)  # Make adminID optional

    def __str__(self):
        return f"Reservation {self.reservationID} - {self.status}"
