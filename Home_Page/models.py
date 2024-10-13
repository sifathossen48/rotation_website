from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Slider(models.Model):
    title = RichTextField()
    description = models.TextField(blank=True,null=True)
    background = models.ImageField(upload_to='slider/')
    button_Link = models.URLField()
    def __str__(self):
        return self.title

class Brand(models.Model):
    website_Link = models.URLField()
    logo = models.FileField(upload_to='brand/')
    def __str__(self):
        return self.website_Link

class Industries(models.Model):
    title = models.CharField(max_length=70)
    icon = models.ImageField(upload_to='Industries/')
    def __str__(self):
        return self.title

class Client(models.Model):
    title = models.CharField(max_length=30)
    image = models.FileField(upload_to='clients/')
    def __str__(self):
        return self.title