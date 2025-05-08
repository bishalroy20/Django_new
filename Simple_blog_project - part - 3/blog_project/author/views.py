from django.shortcuts import render , redirect
from .forms import RegistrationForm  , ChangeUserForm 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
from django.contrib.auth.decorators import login_required
from posts.models import Post

def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("register")
    
    else:
        register_form = RegistrationForm()
    return render(request, 'register.html', {'form': register_form , 'type' : 'register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request ,request.POST )
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name , password = user_pass)
            if user is not None:
                messages.success(request , 'login successfull')
                login(request , user )
                return redirect('profile')
            else:
                messages.success(request , 'Incorrect username and password')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request , 'register.html' , {'form' : form , 'type' : 'login'})
            
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})


def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST , instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request , 'Profile updated successfully')
            return redirect("edit_profile")
    
    else:
        profile_form = ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form': profile_form })



def pass_change(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user , data = request.POST)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request , pass_form.user)
            return redirect("profile")
    
    else:
        pass_form = PasswordChangeForm( user = request.user)
    return render(request, 'pass_change.html', {'form': pass_form })