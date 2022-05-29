from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class DataBlog(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
    title=models.CharField(max_length=200)
    descriptions=models.TextField(max_length=200)

    def __str__(self):
        return self.category.name

