from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Info(models.Model):
    hero_Image = models.ImageField(upload_to='about/')
    chairman_Image = models.ImageField(upload_to='about/')
    chairman_Message = RichTextField()
    about_Image = models.ImageField(upload_to='about/')
    about_Image2 = models.ImageField(upload_to='about/')
    content = RichTextField()
    def __str__(self):
        return "About Page Information"

class Director(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=300)
    profile = models.ImageField(upload_to='directors/')
    twitter = models.URLField(max_length=100)
    facebook = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)
    def __str__(self):
        return self.name