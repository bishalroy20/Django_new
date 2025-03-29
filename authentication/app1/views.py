from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , SetPasswordForm
from django.contrib import messages
from .forms import RegisterForm , ChangeUserData 

# Create your views here.



def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request , "your accout created successfully")
                form.save()
        else:
            form = RegisterForm()
        return render(request , 'signup.html' , {'form': form})
    else:
        return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request , data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name , password = userpass)
                if user is not None:
                    messages.success(request , "Logged In Successfully")
                    login(request , user)
                return redirect("profile")
        else:
            form = AuthenticationForm()
        return render(request , 'login.html' , {'form' : form})
    else:
        return redirect('profile')  


def user_logout(request):
    messages.info(request , "Logged Out Successfully")
    logout(request)
    return redirect('login')


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST , instance = request.user)
            if form.is_valid():
                messages.success(request , 'Account updated')
                form.save()
            
        else:
            form = ChangeUserData( instance = request.user)
        return render(request , 'profile.html' , {'form' : form})
    else:
        return redirect("signup")
    

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request , 'passchange1.html' , {'form': form})


def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user = request.user)
    return render(request , 'passchange1.html' , {'form': form})
