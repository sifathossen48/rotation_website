from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    def __str__(self):
        return self.name