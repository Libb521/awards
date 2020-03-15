from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    class Meta:
        ordering = ['bio']

    def save_user(self):
        self.save()
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    description =models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description