from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        help_text="Required. Must be unique.",
    )
    username = models.CharField(max_length=150, blank=True, null=True)  # Make username optional
    
    USERNAME_FIELD = 'email'  # Using email as the unique identifier
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Excluding password and email

    def __str__(self):
        return self.email