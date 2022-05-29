from django.contrib import admin
from .models import Blog
from .models import Category
from .models import DataBlog
# Register your models here.

admin.site.register(Blog)
admin.site.register(DataBlog)
admin.site.register(Category)