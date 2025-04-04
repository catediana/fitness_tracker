from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet


# urls to route the API endpoints
router = DefaultRouter()
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
