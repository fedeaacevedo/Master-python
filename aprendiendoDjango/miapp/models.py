from django.db import models
from django.db.models.base import Model

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )


class Category(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    created_at = models.DateField()
