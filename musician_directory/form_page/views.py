from django.shortcuts import render , redirect 
from .forms import authorForm
from .models import authorModel
# Create your views here.

def add_author(request):
    if request.method == 'POST':
        form = authorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_author")
    else:
        form = authorForm()
    return render(request , 'add_author.html' , {'form' : form})


def edit_author(request, id):
    post = authorModel.objects.get(pk = id)
    post_form = authorForm(instance=post)
    if request.method == 'POST':
        post_form = authorForm(request.POST , instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("home")
    return render(request , 'add_author.html' , {'form': post_form})

