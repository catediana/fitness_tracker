from django.db import models
from django.db import models
from django.contrib.auth.models import User


# 1. Activity model  containing the fields for logging fitness activities
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    type_of_exercise = models.CharField(max_length=100)
    duration = models.DurationField()
    distance = models.FloatField()
    calories_burned = models.FloatField()  
    date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.type_of_exercise} by {self.user.username}"

