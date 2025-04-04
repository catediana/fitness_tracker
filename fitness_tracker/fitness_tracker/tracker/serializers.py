from rest_framework import serializers
from .models import Activity
from django.contrib.auth.models import User

# 1 . user registration endpoint
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']  # We're only using username and password for registration

    def create(self, validated_data):
        # This method creates the user and hashes the password automatically
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            Email=validated_data['email']
        )
        return user


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'type_of_exercise', 'duration', 'distance', 'calories_burned', 'date', 'user']
        read_only_fields = ['user', 'date']  
