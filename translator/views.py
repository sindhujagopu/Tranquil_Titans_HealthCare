from django.shortcuts import render

def translator_home(request):
    return render(request, 'translator/index.html')
