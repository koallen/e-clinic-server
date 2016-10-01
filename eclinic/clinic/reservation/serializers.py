from rest_framework import serializers
from .models import Reservation
from user_registration.models import Doctor, Patient

class ReservationSerializer(serializers.ModelSerializer):

    doctor = serializers.CharField(read_only=True, source="doctor.get_username")
    patient = serializers.CharField(read_only=True, source="patient.get_username")

    class Meta:
        model = Reservation

class ReservationPostSerializer(serializers.ModelSerializer):
    doctor = serializers.SlugRelatedField(slug_field="user", queryset=Doctor.objects.all())
    patient = serializers.SlugRelatedField(slug_field="user", queryset=Patient.objects.all())

    class Meta:
        model = Reservation

    def create (self, validated_data):
        return Reservation.objects.create(**validated_data)
