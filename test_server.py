
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fitness_tracker.settings")
import django
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    print("Starting Django dev server...")
    django.setup()
    print("Django setup complete!")
    execute_from_command_line(["manage.py", "runserver", "127.0.0.1:8000", "--noreload"])
