from django.shortcuts import render , redirect , get_object_or_404
from .forms import AlbumForm
from .models import Album
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            # form.instance.musician = request.user
            form.save()
            return redirect("add_album")
    else:
        form = AlbumForm()
    return render(request , 'add_album.html' , {'form' : form , 'type' : 'Add '})


@login_required
def edit_album(request, id):
    post = Album.objects.get(pk = id)
    post_form = AlbumForm(instance=post)
    if request.method == 'POST':
        post_form = AlbumForm(request.POST , instance=post)
        if post_form.is_valid():
            # post_form.instance.musician = request.user
            post_form.save()
            return redirect("home")
    return render(request , 'add_album.html' , {'form': post_form , 'type' : 'Edit '})  

# Album() got unexpected keyword arguments: 'instance'
# @login_required
# def edit_album(request, id):
#     post = Album.objects.get(pk = id)
#     post_form = Album(instance=post)
#     if request.method == 'POST':
#         post_form = Album(request.POST , instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect("home")
#     return render(request , 'add_album.html' , {'form': post_form , 'type' : 'Edit Album'})