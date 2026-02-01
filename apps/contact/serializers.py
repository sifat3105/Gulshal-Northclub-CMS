from rest_framework import serializers
from .models import ContactPageImage, Appointment

class ContactPageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPageImage
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

