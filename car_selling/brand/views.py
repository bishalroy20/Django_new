from django.shortcuts import render , redirect
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_brand(request):
    if request.method == 'POST':
        form = forms.BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_brand')
    else:
        form = forms.BrandForm()
    return render(request , 'add_brand.html' , {'form' : form , 'type' : 'Add a Brand name . Add brand '})
   

