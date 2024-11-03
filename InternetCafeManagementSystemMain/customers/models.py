from django.db import models

class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    middleName = models.CharField(max_length=255, blank=True, null=True)
    contactNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.username
