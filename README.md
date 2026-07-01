# 🏋️ GoalFlex

GoalFlex is a full-stack fitness tracking web application built with Django. It enables users to monitor their fitness journey by logging workouts, tracking calories burned, managing personal fitness goals, and visualizing their progress through an interactive dashboard.

The project focuses on creating an intuitive user experience while demonstrating backend development, RESTful API integration, authentication, database management, and responsive frontend design.

---

## 📖 Table of Contents

- Features
- Technologies Used
- Project Structure
- Installation
- Running the Project
- API Overview
- Screenshots
- Future Improvements
- Author
- License

---

# ✨ Features

## Public Website

- Modern landing page
- Responsive navigation
- About section
- Features section
- Testimonials
- User Registration
- User Login

---

## User Authentication

- Secure Registration
- Secure Login
- Logout
- Token Authentication
- Protected Dashboard

---

## Dashboard

The dashboard provides an overview of the user's fitness journey.

Features include:

- User Profile Summary
- Profile Picture
- Gender
- Age
- Height
- Weight
- Fitness Goal
- Total Workouts
- Total Calories Burned
- Total Exercise Time
- Weekly Goal Progress
- Interactive Activity Chart
- Recent Activities Table

---

## Activity Tracking

Users can:

- Browse exercise categories
- Select multiple exercises
- Log workout duration
- Log calories burned
- Log distance
- Save activities
- View activity history

Exercise categories include:

- Running
- Cycling
- Swimming
- Strength Training
- Yoga
- Stretching
- Balance
- Cardio
- Core Exercises
- Warm-up Exercises

---

## Responsive Design

GoalFlex works across:

- Desktop
- Tablet
- Mobile

---

# 🛠 Technologies Used

## Backend

- Python
- Django
- Django REST Framework
- SQLite

---

## Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)
- Chart.js
- Font Awesome

---

## Authentication

- Django Authentication
- Token Authentication

---

## Version Control

- Git
- GitHub

---

# 📁 Project Structure

```
GoalFlex/
│
├── backend/
│
├── frontend/
│
├── static/
│   ├── css/
│   │
│   ├── images/
│   │
│   └── js/
│
├── templates/
│   │
│   ├── layouts/
│   │
│   ├── public/
│   │
│   └── app/
│
├── media/
│
├── db.sqlite3
│
├── manage.py
│
└── README.md
```

---

# 🎨 CSS Architecture

The styling has been organized into reusable modules.

```
static/css/

│
├── shared_styles.css
│
├── variables.css
├── base.css
├── layout.css
├── cards.css
├── components.css
├── forms.css
├── dashboard.css
├── activities.css
├── responsive.css
├── utilities.css
│
├── public.css
└── public_shared.css
```

This modular architecture makes the project easier to maintain, scale, and extend.

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/GoalFlex.git
```

Move into the project

```bash
cd GoalFlex
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

Run the development server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# 📊 Dashboard

The dashboard provides real-time fitness insights.

It includes:

- Profile Overview
- Workout Statistics
- Weekly Goal Progress
- Calories Burned
- Activity Progress Charts
- Recent Activity History

---

# 🏃 Activity Logging

Users can log workouts by selecting exercises from categorized activity lists.

Each activity records:

- Exercise Type
- Duration
- Distance
- Calories Burned
- Date

The information is immediately reflected on the dashboard.

---

# 📡 API

The application exposes RESTful endpoints including:

```
/api/login/

/api/register/

/api/dashboard/

/api/profile/

/api/activities/

/api/exercises/
```

These endpoints are secured using token authentication.

---

# 📱 Responsive Design

GoalFlex has been optimized for different screen sizes.

Supported devices include:

- Desktop
- Laptop
- Tablet
- Mobile

---

# 🚀 Future Improvements

Planned enhancements include:

- Meal Tracking
- Water Intake Tracking
- BMI Calculator
- Weight Progress Graphs
- Achievement Badges
- Workout Recommendations
- AI Fitness Coach
- Notifications & Reminders
- Social Features
- Dark / Light Theme
- Export Progress Reports
- Google Authentication

---

# 📷 Screenshots

Add screenshots of:

- Landing Page
- Login Page
- Registration Page
- Dashboard
- Activities Page
- User Profile

Example

```
screenshots/

home.png

dashboard.png

activities.png

login.png

register.png
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the project

2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 👩‍💻 Author

**Catherine Nanyala**

Computer Scientist | Backend Software Engineer

GitHub:

https://github.com/catediana

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
