from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.CharField('bio', max_length=255, null=True, blank=True)
    image = models.ImageField('image', upload_to='user_profile_images/')