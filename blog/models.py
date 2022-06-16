from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')

    USERNAME_FIELD = 'email'  # Fields that will define the user as unique; we have to mention unique=True in that field
    REQUIRED_FIELDS = ['username']  # we need username inorder to create superuser #Field types that will be asked when we define user via createsuperuser


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name="blogposts_like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.title
