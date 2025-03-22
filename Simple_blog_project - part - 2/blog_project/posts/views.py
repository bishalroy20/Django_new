from django.shortcuts import render , redirect
from .forms import PostForm  
from . import models
from django.contrib.auth.decorators import login_required


@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect("add_post")
    
    else:
        post_form = PostForm()
    return render(request, 'add_post.html', {'form': post_form})



@login_required
def edit_post(request , id):
    post = models.Post.objects.get(pk = id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(request.POST , instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect("add_post")
    return render(request, 'add_post.html', {'form': post_form})


@login_required
def delete_post(request , id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect("home")