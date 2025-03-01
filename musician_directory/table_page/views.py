from django.shortcuts import render , redirect 
from .forms import AlbumForm
from .models import Album

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_album")
    else:
        form = AlbumForm()
    return render(request , 'add_album.html' , {'form' : form})


def edit_album(request, id):
    post = Album.objects.get(pk = id)
    post_form = AlbumForm(instance=post)
    if request.method == 'POST':
        post_form = AlbumForm(request.POST , instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("home")
    return render(request , 'add_album.html' , {'form': post_form})