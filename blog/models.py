from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='media/')
    body = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.title
