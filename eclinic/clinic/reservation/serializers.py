from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):

    doctor = serializers.CharField(read_only=True, source="doctor.get_username")
    patient = serializers.CharField(read_only=True, source="patient.get_username")

    class Meta:
        model = Reservation

    def create (self, validated_data):
        return Reservation.objects.create(**validated_data)
