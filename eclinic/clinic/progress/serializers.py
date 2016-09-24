from rest_framework import serializers
from .models import Progress

class ProgressSerializer(serializers.ModelSerializer):

    doctor = serializers.CharField(read_only=True, source="doctor.get_username")
    patient = serializers.CharField(read_only=True, source="patient.get_username")

    class Meta:
        model = Progress

    def create(self, validated_data):
        """
        Create a new progress
        """
        return Progress.objects.create(**validated_data)
