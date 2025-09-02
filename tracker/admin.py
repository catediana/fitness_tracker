# tracker/admin.py

from django.contrib import admin
from .models import Activity, ExerciseType, UserProfile, ExerciseCategory

# Register your models here.
admin.site.register(ExerciseCategory)
admin.site.register(ExerciseType)
admin.site.register(Activity)
admin.site.register(UserProfile)

