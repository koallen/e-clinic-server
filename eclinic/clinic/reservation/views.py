from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from .models import Reservation
from .serializers import ReservationSerializer, ReservationPostSerializer
from user_registration.models import Doctor, Patient

# Create your views here.

class ReservationList(APIView):

    def post(self, request, format=None):
        """
        create a reservation
        """

        serializer = ReservationPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        """
        Return a list of all reservations.
        """
        username = request.query_params.get('user', None)
        if username is not None:
            reservations = Reservation.objects.filter(doctor__user=username).order_by("datetime")
            if len(reservations) == 0:
                reservations = Reservation.objects.filter(patient__user=username).order_by("datetime")
            serializer = ReservationSerializer(reservations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ReservationDetail(APIView):
    def get_object(self, id):
        try:
            Reservation.objects.get(id=id)
        except Reservation.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        """
        delete a reservation
        """
        reservationToDelete = self.get_object(id)
        reservationToDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
