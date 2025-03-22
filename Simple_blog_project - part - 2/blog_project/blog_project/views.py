from django.shortcuts import render
from posts.models import Post
from categories.models import category


def home(request , category_slug = None): # initially dhore nicchi je category_slug None thakbe karon hocche user first time home page e asle se normal page dekhbe, se filter korte chaile category te click korlei sei category er slug ta capture korbo ar seta tokhn ar None thakbe na
    data = Post.objects.all()# sob post gula ke niye aslam
    if category_slug is not None:
        Category = category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = Category)
    categories = category.objects.all() # sob category dekhabo
    return render(request, 'home.html', {'data' : data, 'category' : categories})

