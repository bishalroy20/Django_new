from django.shortcuts import render
import datetime

def home(request):
    # return render(request , 'index.html')
    # f = {'author' : 'Bishal' , 'age' : '22' , 'lst' : ['python','is','best']}
    # return render(request , 'index.html' , f)
    d = {'Birthday' : datetime.datetime.now()}
    return render(request , 'index.html' , d)

    