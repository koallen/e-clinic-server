from rest_framework import serializers
from .models import MessageToken

class MessageTokenSerializer(serializers.ModelSerializer):
    user = serializers.CharField()

    class Meta:
        model = MessageToken


    def create(self, validated_data):
        """
        create a message token for an existing user
        """
        username = validated_data.get('username')
        try:
            MessageToken.objects.get(user=username)
        except MessageToken.DoesNotExist:
            return MessageToken.objects.create(**validated_data)
        return False

    def update(self, instance, validated_data):
        """
        update a message token
        """
        instance.token = validated_data.get('token', instance.token)
        instance.save()
        return instance

class MessageSerializer(serializers.Serializer):

    from_user = serializers.CharField()
    to_user = serializers.CharField()
    message = serializers.CharField()
