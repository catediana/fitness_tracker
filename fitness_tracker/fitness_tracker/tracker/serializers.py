from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'type_of_exercise', 'duration', 'distance', 'calories_burned', 'date', 'user']
        read_only_fields = ['user', 'date']  
