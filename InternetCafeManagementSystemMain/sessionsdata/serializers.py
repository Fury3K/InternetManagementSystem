from rest_framework import serializers
from .models import SessionData

# Add the missing SessionDataSerializer
class SessionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
       # fields = '__all__'
        fields = ['startTime', 'endTime', 'cost', 'customerID', 'reservationID', 'computerID', 'adminID']
