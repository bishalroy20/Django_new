from django.shortcuts import render , redirect 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout ,update_session_auth_hash
from .forms import RegisterForm , changeuserdata
from django.shortcuts import render , redirect 
from .forms import authorForm
from .models import authorModel

# Create your views here.
@login_required
def add_author(request):
    if request.method == 'POST':
        form = authorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_author")
    else:
        form = authorForm()
    return render(request , 'register.html' , {'form' : form , 'type' : 'Add author'})
    
    
@login_required
def edit_author(request, id):
    post = authorModel.objects.get(pk = id)
    post_form = authorForm(instance=post)
    if request.method == 'POST':
        post_form = authorForm(request.POST , instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("home")
    return render(request , 'register.html' , {'form': post_form , 'type' : 'Edit Author'})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "account created successfully")
            return redirect("register")
    else:
        form = RegisterForm()
    return render(request , 'register.html' , {'form' : form , 'type' : 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = user_name , password = userpass)
            if user is not None:
                messages.success(request , "loged in successfully")
                login(request , user)
                return redirect('profile')
            else:
                messages.warning(request , "incorrect username or password")
                return redirect('register')

    else:
        form = AuthenticationForm()
    return render(request , 'register.html' , { 'form' : form  , 'type' : 'login'})


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        form = changeuserdata(request.POST , instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request , "profile updated successfully")
            return redirect("profile")
    else:
        form = changeuserdata(instance = request.user)
    return render(request , 'profile.html' , {'form' : form , 'type' : 'profile'})
    
