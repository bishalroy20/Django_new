from django.shortcuts import render

from fapp.forms import studentform

# Create your views here.
# def home(request):
#     std = studentform
#     return render(request , 'home.html' , {'form': std})

def home(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = studentform()
    return render(request , 'home.html' , {'form': form})

