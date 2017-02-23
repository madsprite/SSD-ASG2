from django.db import models

from taggit.managers import TaggableManager

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='img/', height_field=2000, width_field=4000)
    username = models.CharField(max_length=20)
    content = models.TextField(max_length=200000, blank=True, null=True)
    tags = TaggableManager()