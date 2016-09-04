from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Doctor, Patient

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=20)
    password = serializers.CharField(required=True, max_length=30)

    def create(self, validated_data):
        """
        Create a user
        """
        return User.objects.create_user(**validated_data)

class PatientRegistrationSerializer(serializers.ModelSerializer){
    class Meta:
        model = Patient

    def create(self, validated_data):
        """
        Register the user as patient
        """
        return Patient.objects.create(**validated_data)
}


class DoctorRegistrationSerializer(serializers.ModelSerializer){
    class Meta:
        model = Doctor

    def create(self, validated_data):
        """
        Register the user as doctor
        """
        return Doctor.objects.create(**validated_data)
}
