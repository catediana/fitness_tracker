from django.shortcuts import render
from rest_framework import viewsets ,permissions
from rest_framework.permissions import IsAuthenticated
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import HTTP_201_CREATED
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser

# 1. register view to Return a Token After Registration

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "User registered successfully!",
            "token": token.key  
        }, status=HTTP_201_CREATED)
    
# 2. ActivityCreateView where users can log their fitness activities 

class ActivityCreateView(generics.CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 3. views that handle the CRUD operations (Create, Read, Update, Delete) for Activity.
class ActivityListView(APIView):
    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    # securing the API  to Ensure that only authenticated users can create, view, update, or delete their activities.
    class ActivityView(APIView):
         permission_classes = [IsAuthenticated]

    def get(self, request):
        activities = Activity.objects.filter(user=request.user)
        return Response({'activities': list(activities.values())})


# 4. filter and sort view 

class ActivityFilter(filters.FilterSet):
    type_of_exercise = filters.CharFilter(field_name='exercise_type__name')
    order_by = filters.OrderingFilter(fields=('date', 'duration', 'distance'))

    class Meta:
        model = Activity
        fields = ['type_of_exercise', 'date', 'duration']

# 5. Activity history view to view detailed history of logged activities
class ActivityHistoryView(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filterset_class = ActivityFilter


# 5. view for admin dashboard where admin can monitor users and activities
class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        activities = Activity.objects.all()
        return Response({'users': list(users.values()), 'activities': list(activities.values())})