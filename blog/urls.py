from django.urls import path
from. import views
urlpatterns = [
            path('', views.home, name='home'),
            path('loginUser/',views.loginUser,name='loginUser'),
            path('logout/',views.logoutpage,name='logout'),
            path('registerPage/',views.registerPage,name='registerPage'),
            path('create_blog/',views.create_blog,name='create_blog'),
            path('show/',views.show,name='show'),

    ]