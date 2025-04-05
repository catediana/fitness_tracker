# Fitness Tracker API

A RESTful API built with Django and Django REST Framework (DRF) for tracking users' physical activities. Users can log exercises, view detailed activity history with filters and sorting, and admins can monitor all user activities.

# Features

- User registration & authentication
- Log physical activities with:
  - Type of exercise
  - Duration
  - Distance
  - Calories burned
  - Timestamp
- View personal activity history with filters and sorting
- Admin dashboard to view all users and activities
- Secure access (only view/edit your own data)
- Django admin support
- Unit tests for key functionality

##  API Endpoints

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/api/register/` | POST | Register new user |
| `/api/login/` | POST | User login |
| `/api/activities/` | GET/POST | List or create user activities |
| `/api/activities/<id>/` | GET/PUT/DELETE | Retrieve, update, or delete an activity |
| `/api/activities/history/` | GET | Filtered and sorted user activity history |
| `/api/admin/dashboard/` | GET | View all users and activities (admin only) |

###  Filtering & Sorting
Available filters:

   1.type_of_exercise
   2.date
   3.duration

Sort by:

  1.date
  2.duration
  3.distance

## Security
1.Authentication required for all activity endpoints
2.Only the activity owner can update/delete
3.Admin-only access to dashboard


## Tests
Tests cover:
    1.User registration and login
    2.Activity creation
    3.Unauthorized access checks

