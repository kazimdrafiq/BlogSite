from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UfserCreationForm
from .models import *
from .forms import * #importing MyUserCreationForm instead of UserCreationForm


def loginUser(request):
    check = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')#.lower()
        password = request.POST.get('password')

        try:
            user = User.objects.filter(email=email)
        except:
            messages.error(request, 'User does not exists!')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            messages.success(request, 'Successfully logged in!')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password do not exist!')

    context = {'check': check}
    return render(request, 'blog/login_register.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')



def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account has been created!')
            login(request, user)
            return redirect('home')
    else:
        messages.error(request, 'Login failed.')
    context = {'form': form}
    return render(request, 'blog/login_register.html', context)



@login_required(login_url='login')
def homePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    all_blogs = Blog.objects.all()
    blogs = Blog.objects.filter(
        Q(categories__name__icontains=q) |
        Q(title__icontains=q) |
        Q(description__icontains=q)
    )
    categories = Categories.objects.all()
    all_blogs_count = all_blogs.count()
    blogs_count = blogs.count()
    context = {'all_blogs': all_blogs, 'blogs': blogs, 'categories': categories, 'all_blogs_count': all_blogs_count, 'blogs_count': blogs_count}
    return render(request, 'blog/home.html', context)



@login_required(login_url='login')
def createBlog(request):
    form = BlogForm()
    categories = Categories.objects.all()

    if request.method == 'POST':
        categories_name = request.POST.get('categories')
        categories = Categories.objects.get(name=categories_name)
        #categories, created_at = Categories.objects.get_or_create(name=categories_name)

        Blog.objects.create(
            author = request.user,
            categories = categories,
            title = request.POST.get('title'),
            description = request.POST.get('description')
        )
        return redirect('home')
    context = {'form': form, 'categories': categories}
    return render(request, 'blog/blog_form.html', context)



@login_required(login_url='login')
def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    categories = Categories.objects.all()

    if request.method == 'POST':
        categories_name = request.POST.get('categories')
        categories = Categories.objects.get(name=categories_name)
        blog.author=request.user
        blog.categories=categories
        blog.title=request.POST.get('title')
        blog.description=request.POST.get('description')
        blog.save()
        return redirect('home')

    context = {'blog':blog, 'form':form, 'categories':categories}
    return render(request, 'blog/blog_form.html', context)



@login_required(login_url='login')
def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == "POST":
        blog.delete()
        return redirect('profile', pk=request.user.id)

    context = {'object': blog}
    return render(request, 'blog/delete-user.html', context)


@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    blogs = user.blog_set.all()
    categories = Categories.objects.all()

    context = {'user': user, 'blogs': blogs, 'categories': categories}
    return render(request, 'blog/profile.html', context)



@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)


    context = {'form': form}
    return render(request, 'blog/update-user.html', context)



@login_required(login_url='login')
def deleteUser(request, pk):
    user = User.objects.get(id=pk)

    if request.method == "POST":
        user.delete()
        return redirect('login')

    context = {'object': user}
    return render(request, 'blog/delete-user.html', context)


@login_required(login_url='login')
def likeCounter(request, pk):
    blog = Blog.objects.get(id=pk)
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)
    return redirect('home')
    return render(request, 'blog/feed_component.html')

