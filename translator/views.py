from django.shortcuts import render,redirect

def translator_home(request):
    return render(request, 'translator/index.html')

def change_language(request, language):
    request.session['language'] = language
    return redirect(f'{language}_dashboard')  # Redirect to the selected language dashboard
