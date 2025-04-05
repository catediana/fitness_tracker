from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import User, Activity
from datetime import timedelta

class ActivityTestCase(TestCase):
    
 def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpassword')
    self.activity = Activity.objects.create(
        user=self.user,
        exercise_type='Running',
        duration=timedelta(minutes=30),
        distance=5.0,
        calories_burned=250
    )


    def test_create_activity(self):
     self.client.login(username='testuser', password='testpassword')
     response = self.client.post(reverse('activity-list'), {
        'exercise_type': 'Cycling',
        'duration': '00:45:00',  
        'distance': 10.0,
        'calories_burned': 350
    })
     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_access(self):
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

