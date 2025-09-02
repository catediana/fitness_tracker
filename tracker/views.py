# tracker/views.py

from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Activity, ExerciseType, UserProfile
from .serializers import ActivitySerializer, UserSerializer, ExerciseTypeSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Sum, F, Count
from django.utils import timezone
from datetime import date, timedelta
from django.utils.dateparse import parse_date
from calendar import monthrange
from collections import defaultdict

# --- New Import for File Uploads ---
from rest_framework.parsers import MultiPartParser, FormParser



# ---------------- Frontend page views ----------------
def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    return render(request, "register.html")

def login_view(request):
    return render(request, "login.html")

def dashboard_view(request):
    return render(request, "dashboard.html")

def activities_view(request):
    return render(request, "activities.html")

def onboarding_view(request):
    return render(request, "onboarding_form.html")


# ---------------- 1. Register view ----------------
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

# ---------------- 2. login ----------------

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            # Delete old token if it exists to prevent token reuse issues
            Token.objects.filter(user=user).delete()
            # Create a new token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"non_field_errors": ["Invalid username or password."]}, status=status.HTTP_400_BAD_REQUEST)

# ---------------- 2. ExerciseType ----------------
class ExerciseTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExerciseType.objects.all()
    serializer_class = ExerciseTypeSerializer
    permission_classes = [IsAuthenticated]


# ---------------- 2. Activity CRUD + history endpoint ----------------
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exercise_types__name', 'date']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        data = self.request.data.copy()
        if "date" in data:
            parsed_date = parse_date(data["date"])
            if parsed_date:
                parsed_date = timezone.make_aware(
                    timezone.datetime.combine(parsed_date, timezone.datetime.min.time())
                )
                serializer.save(user=self.request.user, date=parsed_date)
                return
            else:
                raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        serializer.save(user=self.request.user, date=timezone.now())


# ---------------- 3. Activity filter ----------------
from django_filters import FilterSet

class ActivityFilter(FilterSet):
    class Meta:
        model = Activity
        fields = {
            'exercise_types__name': ['exact', 'icontains'],
            'date': ['exact', 'year', 'month', 'day', 'range'],
            'duration': ['exact', 'gt', 'lt'],
            'distance': ['exact', 'gt', 'lt']
        }


# ---------------- 4. Admin dashboard ----------------
class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        activities = Activity.objects.all()
        activities_serializer = ActivitySerializer(activities, many=True)
        
        return Response({
            'users': list(users.values()),
            'activities': activities_serializer.data
        })


# ---------------- 5. User dashboard summary ----------------
class UserDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        activities = Activity.objects.filter(user=user)

        # Retrieve user profile data
        try:
            user_profile = UserProfile.objects.get(user=user)
            # Pass the request context to the serializer to get the absolute URL
            profile_serializer = UserProfileSerializer(user_profile, context={'request': request})
            profile_data = profile_serializer.data
        except UserProfile.DoesNotExist:
            profile_data = None

        # Summary Stats
        total_workouts = activities.values('date').distinct().count()
        total_duration = activities.aggregate(Sum('duration'))['duration__sum'] or 0
        total_calories = activities.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0

        # Recent Activities (last 5)
        recent_activities = activities.order_by('-date')[:5]
        recent_activities_data = [
            {
                "date": activity.date,
                "exercise_type": ", ".join([ex.name for ex in activity.exercise_types.all()]),
                "distance": activity.distance,
                "duration": activity.duration,
                "calories_burned": activity.calories_burned,
            }
            for activity in recent_activities
        ]

        # Chart Data Logic based on period
        period = request.query_params.get('period', 'weekly')
        today = date.today()
        
        chart_labels = []
        chart_data = []

        if period == 'weekly':
            daily_calories = defaultdict(float)
            local_now = timezone.localtime(timezone.now())
            start_of_week = local_now.date() - timedelta(days=local_now.weekday())
            
            weekly_activities = activities.filter(date__date__gte=start_of_week)

            for activity in weekly_activities:
                local_activity_date = timezone.localtime(activity.date)
                day_index = local_activity_date.weekday()
                daily_calories[day_index] += activity.calories_burned
            
            chart_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            chart_data = [daily_calories[d] for d in range(7)]

        elif period == 'monthly':
            monthly_calories_dict = defaultdict(float)
            
            monthly_activities = activities.filter(
                date__year=today.year
            ).annotate(
                month=ExtractMonth('date')
            ).values('month').annotate(
                total_calories=Sum('calories_burned')
            )
            
            for entry in monthly_activities:
                monthly_calories_dict[entry['month']] = entry['total_calories']
            
            chart_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            chart_data = [monthly_calories_dict.get(m, 0) for m in range(1, 13)]

        elif period == 'yearly':
            yearly_calories_dict = defaultdict(float)
            current_year = today.year
            start_year = current_year - 2
            end_year = current_year + 12
            
            yearly_activities = activities.filter(
                date__year__gte=start_year,
                date__year__lte=end_year
            ).annotate(
                year=ExtractYear('date')
            ).values('year').annotate(
                total_calories=Sum('calories_burned')
            )

            for entry in yearly_activities:
                yearly_calories_dict[entry['year']] = entry['total_calories']

            chart_labels = [str(y) for y in range(start_year, end_year + 1)]
            chart_data = [yearly_calories_dict.get(y, 0) for y in range(start_year, end_year + 1)]
        
        else: # Fallback for invalid period
            daily_calories = defaultdict(float)
            start_of_week = today - timedelta(days=today.weekday())
            weekly_activities = activities.filter(date__date__gte=start_of_week)

            for activity in weekly_activities:
                activity_date = activity.date.date()
                day_index = activity_date.weekday()
                daily_calories[day_index] += activity.calories_burned
            
            chart_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            chart_data = [daily_calories[d] for d in range(7)]

        # Goal Tracking - This logic should be based on the weekly data
        weekly_calorie_goal = 2000
        
        # Recalculate calories this week for goal progress based on the weekly period
        start_of_week = today - timedelta(days=today.weekday())
        calories_this_week = activities.filter(date__date__gte=start_of_week).aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
        
        goal_progress = (calories_this_week / weekly_calorie_goal) * 100
        goal_progress = min(round(goal_progress, 2), 100)

        return Response({
            "username": user.username,
            "profile": profile_data,
            "total_workouts": total_workouts,
            "total_time_minutes": total_duration,
            "total_calories": total_calories,
            "recent_activities": recent_activities_data,
            "chart_labels": chart_labels,
            "chart_data": chart_data,
            "goal_progress": goal_progress,
        })


# ---------------- 6. User Profile (Onboarding) view ----------------
class UserProfileView(APIView):
    # Add parsers to handle form-data requests which include files
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            profile = UserProfile.objects.get(user=user)
            # Pass the request context to the serializer to generate an absolute URL for the image
            serializer = UserProfileSerializer(profile, context={'request': request})
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user = request.user
        # Check if a profile already exists for this user
        if UserProfile.objects.filter(user=user).exists():
            return Response(
                {"error": "Profile already exists. Use PUT to update."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Pass the request context to the serializer
        serializer = UserProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = request.user
        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)

        # Pass the request context and instance to the serializer for updates
        serializer = UserProfileSerializer(profile, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)