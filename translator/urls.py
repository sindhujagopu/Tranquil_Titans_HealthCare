from django.urls import path
from .views import translator_home

urlpatterns = [
    path('', translator_home, name='translator_home'),
    # Add other URL patterns as needed
]
