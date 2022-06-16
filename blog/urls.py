from django.urls import path
from . import views

urlpatterns = [

    #Home Page:
    path('home/', views.homePage, name='home'),

    #Login, Logout:
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    #User Profile (CRUD):
    path('register/', views.registerPage, name='register'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('update-user/', views.updateUser, name='update-user'),
    path('delete-user/<str:pk>/', views.deleteUser, name='delete-user'),

    #Blog (CRUD):
    path('create-blog/', views.createBlog, name='create-blog'),
    path('update-blog/<str:pk>/', views.updateBlog, name='update-blog'),
    path('delete-blog/<str:pk>/', views.deleteBlog, name='delete-blog'),

    #Like Feature:
    path('like/<int:pk>/', views.likeCounter, name='like-view'),
]