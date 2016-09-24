from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProgressSerializer
from .models import Progress

# Create your views here.
class ProgressList(APIView):
    serializer_class = ProgressSerializer;
    def get(self, request, format=None):
        """
        Return a list of all progresses.
        """
        doctorId = request.query_params.get('doctor', None)
        patientId = request.query_params.get('patient', None)
        progresses = Progress.objects.all()
        if (doctorId is not None) and (patientId is not None):
            progresses = progresses.filter(doctor__user=doctorId)
            progresses = progresses.filter(patient__user=patientId)
        serializer = ProgressSerializer(progresses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a new progress
        """
        serializer = ProgressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




