"""
URL configuration for fitness_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.authtoken.views import obtain_auth_token

def welcome_view(request):
    return JsonResponse({
        "message": """
        Welcome to the Fitness Tracker API.

        To get started, visit the following links:

        1. Register: http://127.0.0.1:8000/api/register/
        2. Activities: http://127.0.0.1:8000/api/activities/

        The available activities include:

        1. Log a new fitness activity.
        2. Get all activities for a logged-in user.
        3. Retrieve a specific activity.
        4. Update an activity.
        5. Delete an activity.
        6. View activity history.

        Enjoy tracking your fitness goals!
        """
    })

urlpatterns = [
    path('', welcome_view),
    path('admin/', admin.site.urls),
    path('api/', include('tracker.urls')),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]
