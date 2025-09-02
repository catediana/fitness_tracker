from rest_framework import serializers
from .models import Activity, ExerciseType, UserProfile
from django.contrib.auth.models import User

# 1 . user registration endpoint
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
    
# 2. serializers
class ExerciseTypeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = ExerciseType
        fields = ['id', 'name', 'category_name']


class ActivitySerializer(serializers.ModelSerializer):
    # This nested serializer will display the names of the selected exercises for GET requests
    exercise_types = ExerciseTypeSerializer(many=True, read_only=True)
    
    # This field handles the list of exercise IDs for POST/PUT requests
    exercise_types_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=True,
        help_text="A list of exercise type IDs."
    )
    
    class Meta:
        model = Activity
        fields = ['id', 'exercise_types', 'exercise_types_ids', 'distance', 'duration', 'calories_burned', 'date']
        read_only_fields = ['user']

    def create(self, validated_data):
        # Pop the list of exercise IDs from the validated data
        exercise_types_ids = validated_data.pop('exercise_types_ids')
        
        # Create the new activity instance
        activity = Activity.objects.create(**validated_data)
        
        # Link the selected exercise types to the new activity
        activity.exercise_types.set(exercise_types_ids)
        
        return activity


# 3. UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    # The image field is explicitly defined to ensure it's handled correctly
    profile_photo = serializers.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['gender', 'age', 'height', 'height_unit', 'weight', 'weight_unit', 'fitness_goal', 'activity_level', 'profile_photo']

    def to_representation(self, instance):
        """
        Overrides the default to return the full URL for the image.
        """
        representation = super().to_representation(instance)
        if instance.profile_photo and hasattr(instance.profile_photo, 'url'):
            request = self.context.get('request')
            if request is not None:
                # Use request.build_absolute_uri to construct the full URL
                representation['profile_photo'] = request.build_absolute_uri(instance.profile_photo.url)
            else:
                representation['profile_photo'] = instance.profile_photo.url
        return representation

    def update(self, instance, validated_data):
        # Default ModelSerializer update is sufficient for handling file uploads
        return super().update(instance, validated_data)