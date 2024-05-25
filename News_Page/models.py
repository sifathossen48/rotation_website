from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()
    image = models.ImageField(upload_to='news/')
    def __str__(self):
        return self.title
    
class NewsGallery(models.Model):
    photoName = models.CharField(max_length=30)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='newsGallery/')
    def __str__(self):
        return self.photoName