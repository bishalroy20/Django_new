from django.shortcuts import render
from task.models import addtask

def show_task(request):
    data = addtask.objects.all()
    return render(request , 'show_task.html' , {'form' : data})