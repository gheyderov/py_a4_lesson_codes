from collections.abc import Iterable
from django.db import models
from core.validators import validate_gmail

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbstractModel):
    first_name = models.CharField('first_name', max_length=150)
    email = models.EmailField('email', max_length=155)
    subject = models.CharField('subject', max_length=155)
    message = models.TextField('message')

    def __str__(self):
        return self.first_name
