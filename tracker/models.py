from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# 1. model containing the type of exercise
class ExerciseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExerciseType(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ExerciseCategory, on_delete=models.CASCADE, related_name='exercises')

    def __str__(self):
        return self.name

    
# 2. Activity model containing the fields for logging fitness activities
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    exercise_types = models.ManyToManyField(ExerciseType, related_name='activities')
    
    distance = models.FloatField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    calories_burned = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        exercise_names = ", ".join([ex.name for ex in self.exercise_types.all()])
        return f"{self.user.username}'s activities ({exercise_names}) on {self.date.strftime('%Y-%m-%d')}"


# 3. UserProfile model to store additional user data
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    height_unit = models.CharField(max_length=10, default='cm')
    weight = models.FloatField(null=True, blank=True)
    weight_unit = models.CharField(max_length=10, default='kg')
    fitness_goal = models.CharField(max_length=50, null=True, blank=True)
    activity_level = models.CharField(max_length=50, null=True, blank=True)
    profile_photo = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"