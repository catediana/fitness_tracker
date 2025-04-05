from django.db import models
from django.db import models
from django.contrib.auth.models import User


# 1. model containing the type of exercise
class ExerciseType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name
    
# 2. Activity model  containing the fields for logging fitness activities
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    exercise_type = models.CharField(max_length=100)
    duration = models.DurationField()
    distance = models.FloatField()
    calories_burned = models.FloatField()  
    date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.exercise_type} by {self.user.username}"

