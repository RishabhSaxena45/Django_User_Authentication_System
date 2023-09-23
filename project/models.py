from django.db import models

# Create your models here.
class userdetails(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

class filedetails(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to='media/images')