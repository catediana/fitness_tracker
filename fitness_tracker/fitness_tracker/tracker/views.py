from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# 1. views that handle the CRUD operations (Create, Read, Update, Delete) for Activity.
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        # Filter activities to show only the logged-in user's activities
        return Activity.objects.filter(user=self.request.user)
    

#  2 . user registration view
class RegisterView(APIView):
    def post(self, request):
        # Take the data from the request
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the user to the database
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
