
Fitness Tracker
A full-stack web application designed to help users track their fitness activities and monitor their progress towards personal goals. The project consists of a dynamic front-end dashboard built with HTML, CSS, and JavaScript, and a secure back-end API powered by Django and Django REST Framework.

Table of Contents
Features

Technologies Used

Installation and Setup

Project Structure

API Endpoints

Contributing

License

1. Features
User Management: Secure user registration and login.

Dashboard: A personalized overview displaying key fitness metrics.

Total workouts, calories burned, and total exercise time.

Visual progress bar for weekly calorie goals.

Interactive bar chart to visualize weekly activity.

Responsive table of recent activities.

Activity Logging: Users can add new fitness activities with details such as exercise type, duration, distance, and calories burned.

Data Visualization: Charts and graphs provide insightful visual summaries of fitness data.

Responsive Design: The entire application is optimized for use on desktops, tablets, and mobile devices.

2. Technologies Used
Front-End:

HTML5: Structure of the web pages.

CSS3: Styling and responsiveness.

JavaScript (ES6+): Client-side logic, data fetching, and DOM manipulation.

Chart.js: Library for creating dynamic and responsive charts.

Back-End:

Python 3: The primary programming language.

Django: The high-level Python web framework used for the application's core logic.

Django REST Framework (DRF): A powerful toolkit for building the RESTful API.

SQLite: The default database used for development. 


3. Project Structure
fitness-tracker/
├── venv/                       # Python virtual environment
├── fitness_tracker_project/    # Main Django project directory
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL routing
│   └── ...
├── fitness_app/                # Django app for core functionality
│   ├── models.py               # Database models (User, Activity, etc.)
│   ├── views.py                # Django views and API views
│   ├── urls.py                 # App-specific URL routing
│   ├── serializers.py          # DRF serializers for API data
│   └── ...
├── templates/                  # HTML templates
│   ├── index.html              # The main dashboard page
│   ├── login.html              # Login page
│   ├── register.html           # Registration page
│   └── ...
├── static/                     # CSS, JS, and image files
│   ├── css/
│   ├── js/
│   └── img/
├── manage.py                   # Django's command-line utility
├── requirements.txt            # Python dependencies
└── README.md                   # This file
4. API Endpoints
The API is served by the Django REST Framework. Here are some of the key endpoints:

Endpoint	Method	Description	Authentication
/api/register/	POST	Create a new user account.	None
/api/login/	POST	Authenticate and get an auth token.	None
/api/dashboard/	GET	Retrieve user's dashboard data and stats.	Token
/api/activities/	GET	List all user's activities.	Token
/api/activities/	POST	Create a new activity.	Token
/api/activities/<int:pk>/	GET	Retrieve a single activity by ID.	Token
/api/activities/<int:pk>/	PUT/PATCH	Update an activity.	Token
/api/activities/<int:pk>/	DELETE	Delete an activity.	Token
/api/history/  GET the history of you activities


