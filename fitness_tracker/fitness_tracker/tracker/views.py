from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Activity
from .serializers import ActivitySerializer

# 1. views that handle the CRUD operations (Create, Read, Update, Delete) for Activity.
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        # Filter activities to show only the logged-in user's activities
        return Activity.objects.filter(user=self.request.user)
