from django.shortcuts import render , redirect 
from form_page.models import authorModel
from table_page.models import Album


def home(request):
    musician = authorModel.objects.all()
    album = Album.objects.all()
    context = {
        'data': musician,
        'dataalbum': album,
    }
    return render(request, 'home.html', context)


def delete_author(request , id):
    std = authorModel.objects.get(pk = id).delete()
    # print(std)
    return redirect("home")





