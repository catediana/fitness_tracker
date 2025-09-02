
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from tracker import views as tracker_views 

urlpatterns = [
    # Frontend routes
    path('', tracker_views.index_view, name='index'),
    path('register/', tracker_views.register_view, name='register_page'),
    path('login/', tracker_views.login_view, name='login_page'),
    path('dashboard/', tracker_views.dashboard_view, name='dashboard_page'),
    path('activities/', tracker_views.activities_view, name='activities_page'),
    path('onboarding/', tracker_views.onboarding_view, name='onboarding_page'),

    # Django admin
    path('admin/', admin.site.urls),

    # Tracker app (API routes)
    path('api/', include('tracker.urls')),

    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)