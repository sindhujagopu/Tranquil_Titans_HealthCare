# dashboard/urls.py
from django.urls import path
from .views import english_dashboard, hindi_dashboard, spanish_dashboard,main_dashboard

urlpatterns = [
    path('<str:language>/', english_dashboard, name='english_dashboard'),
    path('<str:language>/hindi/', hindi_dashboard, name='hindi_dashboard'),
    path('<str:language>/spanish/', spanish_dashboard, name='spanish_dashboard'),
    path('main-dashboard/', main_dashboard, name='main_dashboard'),
    # Add other language dashboards as needed
]
