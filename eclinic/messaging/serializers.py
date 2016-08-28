from rest_framework import serializers
from django.contrib.auth.models import User
from models import MessageToken

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = MessageToken
		fields = ('token', 'username')

	
	def create(self, **validated_data):
		"""
		create a message token for an existing user
		"""
		token = validated_data.pop('token')
		username = validated_data.pop('username')
		try:
			MessageToken.objects.get(username = username)
			
		except MessageToken.DoesNotExist:
			return MessageToken.objects.create(**validated_data)
			
		return False




