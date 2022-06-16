from django.contrib import admin
from .models import * #* is importing User as we defined our own user model

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Categories)
