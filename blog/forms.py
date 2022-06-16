from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['host', 'reaction_count']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']