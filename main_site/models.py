from django.db import models
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non Binary'),
        ()
    )
    forename = models.CharField(max_length=24)
    surname = models.CharField(max_length=24)
    created_on = models.DateTimeField(default=timezone.now)
    gender = models.CharField(choices=GENDER_CHOICES)