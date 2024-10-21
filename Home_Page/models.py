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
    
class Category(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
    @property
    def get_brands(self):
        return self.brand_set.all()
class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    website_Link = models.URLField()
    logo = models.FileField(upload_to='brand/')
    background = models.ImageField(upload_to='brand/')
    def __str__(self):
        return self.title
    @property
    def get_products(self):
        return self.product_set.all()
    @property
    def get_galleries(self):
        return self.gallery_set.all()

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,blank=True,null=True)
    description = RichTextField()
    image = models.ImageField(upload_to='products/')
    def __str__(self):
        return self.title
class Gallery(models.Model):
    brand = models.ForeignKey(Brand, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='brand/galleries/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.caption} | {self.brand.title}"
        

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