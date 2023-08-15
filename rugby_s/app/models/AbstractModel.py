from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class BaseUser(AbstractUser):
    
    class Sex(models.TextChoices):
        MALE = 'M', 'male'
        FEMALE = 'F', 'FEMALE'
        OTHER = 'O', 'Other'
    
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now_add=True, blank=True,null=True)

    REQUIRED_FIELDS = ['']


    class Meta:
        abstract = True