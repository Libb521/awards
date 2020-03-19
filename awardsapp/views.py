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
    current_user = request.user
    projects = Projects.objects.all()
    profile = Profile.objects.all()
    image = Image.objects.all()
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
    projects = Projects.objects.all()
    parameter = request.get.get('project')
    get = Projects.objects.filter(project_name__icontains=parameter)
    print(get)
    return render(request, 'search.html', locals())

def project(request, project_id):
    try:
        this_project = Projects.objects.get(id=project_id)
        print(this_project)
    except Project.DoesNotExist:
        raise Http404()
    return render(request, 'project.html', locals())

def upload_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.post, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(requesr, 'upload.html', {'uploadform': form})

