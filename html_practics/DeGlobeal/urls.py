from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('updates/', views.updates, name='updates'),
    path('cv_page/', views.cv_page, name='cv_page'),
    path('certificate/', views.certificate, name='certificate'),
    path('about/', views.about, name='about'),
    path('social/', views.social, name='social'),
    path('email/', views.email, name='email'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
]
