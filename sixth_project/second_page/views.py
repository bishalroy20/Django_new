from django.shortcuts import render , redirect
from . import models


def home(request):
    student = models.student.objects.all()
    print(student)
    return render(request , 'home.html' , {'data' : student})

def delete_student(request , roll):
    std = models.student.objects.get(pk = roll).delete()
    print(std)
    return redirect("home")