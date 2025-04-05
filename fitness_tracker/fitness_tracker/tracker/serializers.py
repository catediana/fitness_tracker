from rest_framework import serializers
from .models import Activity ,ExerciseType
from django.contrib.auth.models import User

# 1 . user registration endpoint
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password','email']  

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
    
# 2. serializers
class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    exercise_type = ExerciseTypeSerializer()
    class Meta:
        model = Activity
        fields = ['id', 'exercise_type', 'duration', 'date','distance']
