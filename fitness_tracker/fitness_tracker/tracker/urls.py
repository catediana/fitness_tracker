from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, UserDashboardView 

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activities')

urlpatterns = [
    path('dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
    path('activities/history/', ActivityViewSet.as_view({'get': 'history'}), name='activities-history'),
]

urlpatterns += router.urls
