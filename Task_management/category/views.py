from django.shortcuts import render , redirect
from . import forms


def add_category(request):
    if request.method == 'POST':
        add_form = forms.category_Form(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect("add_category")
    else:
        add_form = forms.category_Form()
        return render(request , 'add_category.html' , {'form' : add_form})