from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MessageToken

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = MessageToken
		fields = ('token', 'username')

	
	def create(self, **validated_data):
		"""
		create a message token for an existing user
		"""
		try:
			MessageToken.objects.get(username = validated_data.get('username'))
			
		except MessageToken.DoesNotExist:
			return MessageToken.objects.create(**validated_data)
			
		return False

	def update(self, instance, **validated_data):
		"""
    	update a message token
    	"""
		instance.token = validated_data.get('token', instance.token)
		instance.save()
		return True





