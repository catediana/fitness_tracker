
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, RegisterView

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activities')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]

# Add the router-generated URLs
urlpatterns += router.urls
