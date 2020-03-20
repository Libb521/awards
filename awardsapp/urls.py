from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from awardsapp import views as awardsapp_views
from . import views

urlpatterns=[
    path('',views.home,name ='home'),
    path('profile/',views.profile,name = 'profile'),
    path('form/',views.upload_form,name = 'upload_form'),
    path('search/',views.search,name = 'search'),
    path('update/',views.edit_prof,name='update_profile'),
    path('signup/', views.signup,name='signup'),
    path('project/', views.project,name='project'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('api/projects', views.ProjectList.as_view()),
    path('api/profiles', views.ProfileList.as_view()),
    re_path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)