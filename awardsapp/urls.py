from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from awardsapp import views as awardsapp_views
from . import views

urlpatterns=[
    path('',views.home,name ='home'),
    path('newprofile/',views.profile,name = 'profile'),
    path('form/',views.upload_form,name = 'upload_form'),
    path('new-project/', views.postproject, name='newproject'),
    path('search/',views.search,name = 'search'),
    # path('showprofile/',views.display_profile,name = 'showprofile'),
    path('signup/', views.signup,name='signup'),
    # path('add_image/', views.add_image, name = 'add_image'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    re_path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)