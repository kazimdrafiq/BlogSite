from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import ShowForm
from .models import DataBlog


def home(request):
    return render(request, 'home.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, ' User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User Password doesn not exist')
    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error during the registration")

    return render(request, 'registration.html', {'form': form})


def create_blog(request):
    form = ShowForm()
    if request.method == "POST":
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show")
    context = {'form': form}
    return render(request, "create_message.html", context)

def show(request):
    values=DataBlog.objects.all()
    context={'values':values}
    return render(request,'home.html',context)