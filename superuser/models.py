from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class about(models.Model):
    content = RichTextUploadingField()