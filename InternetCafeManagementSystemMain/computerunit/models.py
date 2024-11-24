from django.db import models

class ComputerUnit(models.Model):
    computerID = models.AutoField(primary_key=True)
    availability = models.BooleanField(default=True)
    adminID = models.ForeignKey('admin_app.Admin', on_delete=models.CASCADE)

    def __str__(self):
        return f"Computer {self.computerID} - {'Available' if self.availability else 'Unavailable'}"
