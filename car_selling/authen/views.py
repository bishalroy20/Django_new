from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import RegisterForm , ChangeUserData
from django.contrib.auth.decorators import login_required
from car.models import Car , Purchase

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request , 'account created successfully')
            form.save()

    else:
        form = RegisterForm()
    return render(request , 'register.html' , {'form': form , 'type' : 'Signup'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request , data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name , password = userpass)
            if user is not None:
                login(request,user)
                return redirect("profile")
    else:
        form = AuthenticationForm()
        return render(request , 'register.html' , {'form': form , 'type' : 'Login'})
    



def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login') 


@login_required
def profile(request):
    data = Car.objects.filter(name = request.user)
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, 'profile.html', {'data' : data , 'purchases': purchases})



def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST , instance = request.user)
        if form.is_valid():
            messages.success(request , 'profile edited successfully')
            form.save()

    else:
        form = ChangeUserData(instance = request.user)
    return render(request , 'register.html' , {'form': form , 'type' : 'Edit your profile'} )
    
