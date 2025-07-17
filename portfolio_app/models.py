# portfolio_app/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

from django.db import models
from twilio.rest import Client
from django.conf import settings
from django.contrib.auth.models import User  # Import the User model



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default="No Subject")  # Default value
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Add a field to track whether the message has been read
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Add the user field

    def __str__(self):
        return self.name
    

class FeaturedProject(models.Model):
    CATEGORY_CHOICES = [
        ('UI/UX', 'UI/UX Design'),
        ('Web', 'Web Development'),
        ('Photo', 'Photography'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Web')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title