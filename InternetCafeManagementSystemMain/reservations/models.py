from django.db import models

class Reservations(models.Model):
    reservationID = models.AutoField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    status = models.CharField(max_length=100)
    adminID = models.ForeignKey('admin_app.Admin', on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation {self.reservationID} - {self.status}"
