from django.shortcuts import render , redirect
from .forms import profile_form
# Create your views here.

def add_profile(request):
    if request.method == 'POST':
        profileform = profile_form(request.POST)
        if profileform.is_valid():
            profileform.save()
            return redirect("add_profile")
    else:
        profileform = profile_form()
    return render(request , 'add_profile.html' , {'form' : profileform})