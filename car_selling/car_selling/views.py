from django.shortcuts import render,redirect , get_object_or_404
from car.models import Car, Purchase
from brand.models import Brand
from django.views.generic import DetailView
from car.forms import CommentForm
from django.contrib import messages


def home(request, category_slug=None):
    data = Car.objects.all()  
    brand_category = None 

    if category_slug:
        brand_category = Brand.objects.get(slug=category_slug) 
        data = Car.objects.filter(brand_name=brand_category)  

    categories = Brand.objects.all() 
    
    return render(request, 'home.html', {'data': data, 'category': categories, 'brand_category': brand_category})




class CarDetailView(DetailView):
    model = Car
    pk_url_kwarg = 'id' 
    template_name = 'details.html'

    def post(self, request, *args, **kwargs):  
        car = self.get_object()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car  
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all() 
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    



def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id) 
    if car.quantity > 0:
        car.quantity -= 1  
        car.save()  
        Purchase.objects.create(user=request.user, car=car)
        messages.success(request, f"You have successfully purchased {car.name}!")
    else:
        messages.error(request, f"Sorry, {car.name} is out of stock.")
    
    return redirect('home') 


