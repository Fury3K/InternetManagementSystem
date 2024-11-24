from django.db import models

class CustomerFeedback(models.Model):
    feedbackID = models.AutoField(primary_key=True)
    customerFeedback = models.CharField(max_length=500)
    customerID = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, related_name='customer_feedbacks')
    adminID = models.ForeignKey('admin_app.Admin', on_delete=models.CASCADE)

    def __str__(self):
        return f"Feedback {self.feedbackID}"
