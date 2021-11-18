from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

import random ,string
def get_random_string(size):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = size))
def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    slug=slugify(new_slug)[:50]
    Klass = instance
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = slugify(str(slug)[:46]+get_random_string(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug



class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(Category,self.name)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.name)
class Couses(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="Couses")
    img = models.ImageField(upload_to="couses")
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    target = models.FloatField()
    raised = models.FloatField()
    content = RichTextUploadingField()
    time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(Couses,self.title)
        super(Couses, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.title)
