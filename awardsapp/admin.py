from django.contrib import admin
from .models import Profile, Image, Projects

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('Profile',)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Projects)