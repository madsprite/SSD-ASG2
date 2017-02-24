from django.db import models
from django.

class ProfileAvatar(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')

class User(models.Model):
   username = models.CharField(max_length = 20, primary_key = True)
   name = models.CharField(max_length = 20)
   email = models.CharField(max_length = 40)
   password = models.CharField(max_length = 200)
   salt = models.CharField(max_length = 20)