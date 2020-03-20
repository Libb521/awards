from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .models import Projects, Image, Profile
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='login')
def home(request):
    current_user = request.user
    projects = Projects.objects.all()
    profile = Profile.objects.all()
    image = Image.objects.all()
    return render(request, 'index.html')

@login_required(login_url='login')
def profile(request):
    current_user = request.user
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect( 'profile')
    else:
        form = ProfileForm()
        my_projects = Projects.objects.filter(repo_owner=current_user)
        my_profile = Profile.objects.get(user_id=current_user)
    return render(request, 'profile.html', locals())

@login_required(login_url='login')
def search(reques):
    projects = Projects.objects.all()
    parameter = request.GET.get("project")
    result = Projects.objects.filter(project_name__icontains=parameter)
    print(result)
    return render(request, 'search.html', locals())

@login_required(login_url='login')
def project(request, project_id):
    try:
        this_project = Projects.objects.get(id=project_id)
        print(this_project)
    except Project.DoesNotExist:
        raise Http404()
    return render(request, 'project.html', locals())

@login_required(login_url='login')
def upload_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


@login_required(login_url='login')
def edit_prof(request):
    
    current_user = request.user
    user = User.objects.all()
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id=current_user
            return redirect('home')
    else:
        form = UpdateProfileForm()
        return render(request,'profile_edit.html',{'user':user,'form':form})

@login_required(login_url='login')
def logout_view(request):
    logout(request)