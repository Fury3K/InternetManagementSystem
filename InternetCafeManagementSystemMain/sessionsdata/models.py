from django.db import models
from customers.models import Customer  
from reservations.models import Reservations
from computerunit.models import ComputerUnit  
from admin_app.models import Admin  

# Session Data model
class SessionData(models.Model):
    sessionID = models.AutoField(primary_key=True)
    startTime = models.TimeField()
    endTime = models.TimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservationID = models.ForeignKey(Reservations, on_delete=models.CASCADE)
    computerID = models.ForeignKey(ComputerUnit, on_delete=models.CASCADE)  # Corrected to ComputerUnit
    adminID = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self):
        return f"Session {self.sessionID} - Customer {self.customerID}"
