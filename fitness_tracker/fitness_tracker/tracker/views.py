from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

# 1. Register view
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


# 2. Activity CRUD + history endpoint
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activity_type', 'date']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='history')
    def history(self, request):
        """
        Returns the user's activities history.
        """
        activities = self.filter_queryset(self.get_queryset().order_by('-date'))
        serializer = self.get_serializer(activities, many=True)
        return Response(serializer.data)


# 3. Activity filter (optional for advanced filtering)
class ActivityFilter(filters.FilterSet):
    type_of_exercise = filters.CharFilter(field_name='exercise_type__name')
    order_by = filters.OrderingFilter(fields=('date', 'duration', 'distance'))

    class Meta:
        model = Activity
        fields = ['type_of_exercise', 'date', 'duration']


# 4. Admin dashboard
class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        activities = Activity.objects.all()
        return Response({
            'users': list(users.values()),
            'activities': list(activities.values())
        })


# 5. User dashboard summary
class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        activities = Activity.objects.filter(user=request.user)
        total_activities = activities.count()
        total_duration = sum(a.duration for a in activities)
        
        total_steps = total_duration
        total_calories = total_duration  

        return Response({
            "steps": total_steps,
            "calories": total_calories,
            "workouts": total_activities
        })
