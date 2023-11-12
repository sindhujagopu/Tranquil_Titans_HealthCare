from django.urls import path
from .views import translator_home,change_language

urlpatterns = [
    path('', translator_home, name='index'),
    path('change-language/<str:language>/', change_language, name='change_language'),
    # Add other URL patterns as needed
]
