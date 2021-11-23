from django.db import models
from django.db.models.enums import Choices
from couses.models import Category,unique_slug_generator
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    choices = (
    ('News','News'),
    ('Blog','Blog'),
    )
    type = models.CharField(max_length=5,choices=choices)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="Blog")
    time = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to = 'News-Blog')
    title = models.CharField(max_length=150)
    shortDes = models.CharField(max_length=200)
    content = RichTextUploadingField()
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(Blog,self.title)
        super(Blog, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.title)