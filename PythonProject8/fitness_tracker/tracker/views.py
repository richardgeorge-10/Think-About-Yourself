from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'tracker/home.html')

def dashboard(request):
    return render(request, 'tracker/dashboard.html')

def workouts(request):
    return render(request, 'tracker/workouts.html')

def nutrition(request):
    return render(request, 'tracker/nutrition.html')

def community(request):
    return render(request, 'tracker/community.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})