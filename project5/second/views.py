from django.shortcuts import render
from . forms import contactform


def contact(request):
    return render(request , 'second/contact.html' )

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request , 'second/about.html' , {'name' : name , 'email' : email , 'select' : select})
    else:
        return render(request , 'second/about.html' )
    
    # return render(request , 'second/about.html'  )
    
    


def form(request):
    # print(request.POST)
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     return render(request , 'second/form.html' , {'name' : name , 'email' : email})
    # else:
    return render(request , 'second/form.html' )
    

# def Django_form(request):
#     form = contactform(request.POST)
#     if form.is_valid():
#         print(form.cleaned_data)
#     return render(request , 'second/django_form.html' , {'form' : form})


#file upload code#
def Django_form(request):
    if request.method == 'POST':
        form = contactform(request.POST , request.FILES)
        if form.is_valid():
            # file= form.cleaned_data['file']
            # with open('second/upload/' + file.name , 'wb+') as destination:
            #     for chunck in file.chunks():
            #         destination.write(chunck)
            print(form.cleaned_data)
            return render(request , 'second/django_form.html' , {'form' : form})
    else:
        form = contactform()
    return render(request , 'second/django_form.html' , {'form': form})

