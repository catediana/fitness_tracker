from django.core.management.base import BaseCommand
from tracker.models import ExerciseCategory, ExerciseType


class Command(BaseCommand):
    help = "Populate exercise categories and exercise types"

    def handle(self, *args, **kwargs):

        data = {
            "Strength Exercises": [
                "Push-ups",
                "Squats",
                "Lunges",
                "Deadlifts",
                "Bench Press",
                "Bicep Curls",
                "Plank Hold",
            ],

            "Aerobic Exercises": [
                "Running",
                "Cycling",
                "Swimming",
                "Jump Rope",
                "HIIT",
                "Dancing / Zumba",
            ],

            "Flexibility Exercises": [
                "Yoga Poses",
                "Hamstring Stretch",
                "Quadriceps Stretch",
                "Shoulder Stretch",
                "Cat-Cow Stretch",
            ],

            "Balance Exercises": [
                "Single-Leg Stand",
                "Heel-to-Toe Walk",
                "Bosu Ball Balance",
                "Side Leg Raises",
                "Tai Chi Movements",
            ],

            "Core Exercises": [
                "Sit-ups / Crunches",
                "Russian Twists",
                "Mountain Climbers",
                "Leg Raises",
                "Bicycle Crunches",
            ],

            "Mobility Exercises": [
                "Arm Circles",
                "Hip Circles",
                "Shoulder Rolls",
                "Ankle Circles",
                "Dynamic Lunges",
            ],

            "Endurance Exercises": [
                "Long-distance Running",
                "Rowing",
                "Stair Climbing",
                "Hiking",
                "Swimming Laps",
            ],
        }

        categories_created = 0
        exercises_created = 0

        for category_name, exercises in data.items():

            category, created = ExerciseCategory.objects.get_or_create(
                name=category_name
            )

            if created:
                categories_created += 1

            for exercise in exercises:

                _, created = ExerciseType.objects.get_or_create(
                    name=exercise,
                    category=category,
                )

                if created:
                    exercises_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done! Added {categories_created} categories and {exercises_created} exercises."
            )
        )