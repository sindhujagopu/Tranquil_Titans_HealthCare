# dashboard/views.py
from django.shortcuts import render

def english_dashboard(request, language):
    return render(request, 'dashboard/english_dashboard.html', {'language': language})

def hindi_dashboard(request, language):
    return render(request, 'dashboard/hindi_dashboard.html', {'language': language})

def spanish_dashboard(request, language):
    return render(request, 'dashboard/spanish_dashboard.html', {'language': language})
def main_dashboard(request):
    language = request.session.get('language', 'en')  # Default to 'en' if language is not set
    dashboard_template = f'dashboard/{language}_dashboard.html'
    return render(request, dashboard_template, {'language': language})