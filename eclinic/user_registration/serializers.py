from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=20)
    password = serializers.CharField(required=True, max_length=30)

    def create(self, validated_data):
        """
        Create a user
        """
        return User.objects.create_user(**validated_data)
