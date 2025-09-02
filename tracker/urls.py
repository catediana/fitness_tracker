# tracker/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ActivityViewSet, 
    UserDashboardView, 
    ExerciseTypeViewSet, 
    LoginView,
    RegisterView, # You need to import this here
    UserProfileView # You need to import this here
)

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'exercises', ExerciseTypeViewSet, basename='exercises')

urlpatterns = [
    # API endpoints
    path('register/', RegisterView.as_view(), name='api_register'),
    path('login/', LoginView.as_view(), name='api_login'), 
    path('user-profile/', UserProfileView.as_view(), name='api_user_profile'),
    path('dashboard/', UserDashboardView.as_view(), name='api_user_dashboard'),
    
]

urlpatterns += router.urls