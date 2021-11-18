from django.db import models
from django.db.models.base import Model

from couses.models import unique_slug_generator
from galleryfield.fields import GalleryField
# Create your models here.
from couses.models import Category

class Events(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE , related_name="Events")
    title = models.CharField(max_length=100)
    eventTime = models.DateTimeField()
    Address = models.CharField(max_length=500)
class eventImg(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE,related_name="eventImg")
    img = models.ImageField(upload_to="eventImg")








































