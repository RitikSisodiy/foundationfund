from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class VolunteerRegister(models.Model):
    choices = (
        ( 'Applied','Applied' ),
        ( 'Reviewed','Reviewed' ),
        ( 'Pending','Pending' ),
        ( 'Verified','Verified' ),
    )
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    branch = models.CharField(max_length=40)
    message = models.CharField(max_length=40)
    resume = models.FileField(upload_to='resume')
    status = models.CharField(max_length=20,choices=choices,default="Applied")