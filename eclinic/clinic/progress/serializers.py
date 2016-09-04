from rest_framework import serializers
from .models import Progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress

    def create(self, validated_data):
        """
        Create a new progress
        """
        return MessageToken.objects.create(**validated_data)
