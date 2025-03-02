from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name='login'),  # Login page
    path('', views.home, name='home'),  # Home page
]