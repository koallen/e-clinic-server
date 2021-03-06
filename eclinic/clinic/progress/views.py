from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProgressSerializer, ProgressPostSerializer
from .models import Progress

# Create your views here.
class ProgressList(APIView):

    def get(self, request, format=None):
        """
        Return a list of all progresses.
        """
        doctorId = request.query_params.get('doctor', None)
        patientId = request.query_params.get('patient', None)
        progresses = Progress.objects.all()
        if (doctorId is not None) and (patientId is not None):
            progresses = progresses.filter(doctor__user=doctorId)
            progresses = progresses.filter(patient__user=patientId).order_by("datetime")
        serializer = ProgressSerializer(progresses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new progress
        """
        serializer = ProgressPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




