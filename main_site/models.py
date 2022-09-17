from pydoc import describe
from django.db import models
from django.utils import timezone
from .choices import GENDER_CHOICES

# Create your models here.

class Client(models.Model):
    "Single person users on our websites"
    forename = models.CharField(max_length=24)
    surname = models.CharField(max_length=24)
    created_on = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=256, null=True, blank=True)
    password = models.CharField(max_length=256, null=True, blank=True)
    verification = models.BooleanField(default=False)

class Policies(models.Model):
    "Actions people can take to help their carbon footprint"
    created_on = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
