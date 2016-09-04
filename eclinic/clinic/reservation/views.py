from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Reservation
from .serializers import ReservationSerializer

# Create your views here.

class ReservationList(APIView):

    def post(self, request, format=None):
        """
        create a reservation
        """
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request, format=None):
        """
        Return a list of all reservations.
        """
        serializer = ReservationSerializer(data=Reservation.objects.all())
        return Response(serializer.data, status=status.HTTP_200_OKEY)


class ReservationDetail(APIView):

    def delete(self, request, id, format=None):
        """
        delete a reservation
        """
        reservationToDelete = self.get_object(id)
        reservationToDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)