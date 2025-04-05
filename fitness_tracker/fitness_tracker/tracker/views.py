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
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.status import HTTP_201_CREATED

# 1. views that handle the CRUD operations (Create, Read, Update, Delete) for Activity.
class ActivityListView(APIView):
    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


# 2. register view to Return a Token After Registration

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Create the user and handle response
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generating a token for the new user
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "User registered successfully!",
            "token": token.key  
        }, status=HTTP_201_CREATED)





# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer

class ActivityListView(APIView):
    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
