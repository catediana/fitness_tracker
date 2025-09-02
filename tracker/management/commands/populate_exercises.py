from django.core.management.base import BaseCommand
from tracker.models import ExerciseCategory, ExerciseType

class Command(BaseCommand):
    help = 'Populates ExerciseCategory and ExerciseType with initial data'

    def handle(self, *args, **kwargs):
        ExerciseType.objects.all().delete()
        ExerciseCategory.objects.all().delete()

        data = {
            "Strength Exercises": [
                "Push-ups", "Squats", "Lunges", "Deadlifts", "Bench Press", "Bicep Curls", "Plank Hold"
            ],
            "Aerobic Exercises": [
                "Running", "Cycling", "Swimming", "Jump Rope", "HIIT", "Dancing / Zumba"
            ],
             "Flexibility Exercises": [
        "Yoga Poses", "Hamstring Stretch", "Quadriceps Stretch", "Shoulder Stretch", "Cat-Cow Stretch"
            ],
       "Balance Exercises": [
             "Single-Leg Stand", "Heel-to-Toe Walk", "Bosu Ball Balance", "Side Leg Raises", "Tai Chi Movements"
            ],
        "Core Exercises": [
            "Sit-ups / Crunches", "Russian Twists", "Mountain Climbers", "Leg Raises", "Bicycle Crunches"
            ],
       "Mobility Exercises": [
           "Arm Circles", "Hip Circles", "Shoulder Rolls", "Ankle Circles", "Dynamic Lunges"
            ],
        "Endurance Exercises": [
           "Long-distance Running", "Rowing", "Stair Climbing", "Hiking", "Swimming Laps"
    ]
}

        

        for category_name, exercises in data.items():
            category = ExerciseCategory.objects.create(name=category_name)
            for ex in exercises:
                ExerciseType.objects.create(name=ex, category=category)

        self.stdout.write(self.style.SUCCESS('Categories and exercises populated successfully!'))
