from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        add_form = forms.addForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect("add_task")
    else:
        add_form = forms.addForm() 
    return render(request, 'add_task.html', {'form': add_form})


def edit_task(request , id):
    post = models.addtask.objects.get(pk = id)
    post_form = forms.addForm(instance=post)
    if request.method == 'POST':
        post_form = forms.addForm(request.POST , instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("show_task")
    else:
        return render(request, 'add_task.html', {'form': post_form})

def delete_task(request , id):
    post = models.addtask.objects.get(pk=id)
    post.delete()
    return redirect("show_task")
