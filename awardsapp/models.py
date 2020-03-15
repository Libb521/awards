from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    