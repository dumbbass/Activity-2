from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
] 