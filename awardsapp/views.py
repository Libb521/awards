from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .models import Projects, Image, Profile
from django.http import HttpResponse, Http404

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'index.html')


def profile(request):
    current_user = request.user
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect( 'profile')
    else:
        form = ProfileForm()
        my_projects = Projects.objects.filter(owner=current_user)
        my_profile = profile.objects.get(user_id=current_user)
    return render(request, 'profile.html', locals())

def search(reques):
    if request.method =='POST':
        form = SearchForm(request,POST)
    return render(request, 'search.html')