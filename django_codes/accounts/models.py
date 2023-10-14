from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from core.models import AbstractModel


# Create your models here.

class User(AbstractUser):
    bio = models.CharField('bio', max_length=255, null=True, blank=True)
    image = models.ImageField('image', upload_to='user_profile_images/', null=True, blank=True)
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/static/images/nophoto.jpeg/'
        

class BlockedIps(AbstractModel):
    ip_address = models.GenericIPAddressField()