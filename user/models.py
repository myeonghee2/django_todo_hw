from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile = models.TextField(null=True, blank=True)

# class Userprofile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_image = models.ImageField(upload_to='profile_image/')