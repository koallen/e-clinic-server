from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegistrationSerializer
from .serializers import DoctorRegistrationSerializer
from .serializers import PatientRegistrationSerializer
from .models import Doctor

class UserList(APIView):
    """
    Create a new user
    """
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # handle user registration
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorList(APIView):
    """
    Create a new doctor
    """
    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorRegistrationSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # handle doctor registration
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientList(APIView):
    """
    Create a new patient
    """
    def post(self, request, format=None):
        serializer = PatientRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # handle patient registration
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
