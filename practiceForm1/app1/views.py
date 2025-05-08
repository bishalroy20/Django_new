from django.shortcuts import render
from .forms import practiceform , practicemodelform

# Create your views here.
def home(request):
    form = practiceform
    return render(request , 'home.html' , {'form' : form})


def home2(request):
    form = practicemodelform
    return render(request, 'home2.html', {'form': form})
