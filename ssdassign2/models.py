from django.db import models

class ProfileAvatar(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'avatars', height_field=2000, width_field=4000)

class Users(models.Model):
   username = models.CharField(max_length = 20, primary_key = True)
   name = models.CharField(max_length = 20)
   email = models.CharField(max_length = 40)
   password = models.CharField(max_length = 200)
   salt = models.CharField(max_length = 20)

   class Meta:
   		db_table = 'users'
   	
   		