from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProgressSerializer
from .models import Progress

# Create your views here.
class ProgressList(APIView):

    def get(self, request, format=None):
        """
        Return a list of all progresses.
        """
        progresses = Progress.objects.all()
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

