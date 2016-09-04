from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
	 class Meta:
        model = Reservation


        def create (self, validated_data):
        	return Reservation.objects.create(**validated_data)