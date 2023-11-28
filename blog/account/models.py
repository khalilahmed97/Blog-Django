from django.db import models 
from django.contrib.auth.models import AbstractBaseUser

    
class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=255)

  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
