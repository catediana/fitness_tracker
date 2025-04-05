from rest_framework import serializers
from .models import Activity
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


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'type_of_exercise', 'duration', 'distance', 'calories_burned', 'date', 'user']
        read_only_fields = ['user', 'date']  
