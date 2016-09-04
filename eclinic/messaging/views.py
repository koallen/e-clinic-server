from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from .models import MessageToken
from .serializers import MessageTokenSerializer, MessageSerializer

class MessageTokenList(APIView):

    def post(self, request, format=None):
        """
        create a message token for an existing user
        """
        serializer = MessageTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageTokenDetail(APIView):
    def get_object(self, id):
        try:
            return MessageToken.objects.get(id = id)
        except MessageToken.DoesNotExist:
            raise Http404

    def patch(self, request, id, format=None):
        """
        update a message token
        """
        messageToken = self.get_object(id)
        serializer = MessageTokenSerializer(messageToken, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageList(APIView):

    def post(self, request, format=None):
        """
        Accept message from one user and send it to the destination
        """
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            from_user = serializer.validated_data["from_user"]
            to_user = serializer.validated_data["to_user"]
            message = serializer.validated_data["message"]
