# dashboard/views.py
from django.shortcuts import render

def english_dashboard(request, language):
    return render(request, 'dashboard/english_dashboard.html', {'language': language})

def hindi_dashboard(request, language):
    return render(request, 'dashboard/hindi_dashboard.html', {'language': language})

def spanish_dashboard(request, language):
    return render(request, 'dashboard/spanish_dashboard.html', {'language': language})

