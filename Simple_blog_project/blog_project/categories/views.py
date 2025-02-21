from django.shortcuts import render , redirect
from .forms import categoryForm  


def add_category(request):
    if request.method == 'POST':
        category_form = categoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect("add_category")
    
    else:
        category_form = categoryForm()
    return render(request, 'add_category.html', {'form': category_form})
