from django.shortcuts import render , get_object_or_404
from django.views.generic import TemplateView
from product.models import Product
from product.forms import CommentForm
from category.models import Sport
from django.views.generic import DetailView
from django.http import JsonResponse
# Create your views here.

def home(request, category_slug=None):
    data = Product.objects.all()  
    brand_category = None 

    if category_slug:
        brand_category = Sport.objects.get(slug=category_slug) 
        data = Product.objects.filter(sport_name=brand_category)  # Corrected field name

    categories = Sport.objects.all()  
    
    return render(request, 'homepage.html', {'data': data, 'category': categories, 'brand_category': brand_category})



def filter_by_category(request, category_slug):
    try:
        # Get the category by its slug
        brand_category = get_object_or_404(Sport, slug=category_slug)
        
        # Filter the products by the category
        products = Product.objects.filter(sport_name=brand_category)
        
        # Create a list of dictionaries to send as JSON response
        data = [
            {
                "id": p.id,
                "name": p.name,
                "price": str(p.price),  # Make sure price is a string
                "image": p.image.url if p.image else None,  # Handle missing images
                "sport_name": p.sport_name.name if p.sport_name else "",
            }
            for p in products
        ]
        
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)



class CarDetailView(DetailView):
    model = Product
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
    





def search_products(request):
    query = request.GET.get('q', '')  # Get user input from search box
    products = Product.objects.filter(name__icontains=query) if query else []

    # Convert Product objects to JSON format
    data = [{"id": p.id, "name": p.name, "price": str(p.price)} for p in products]  # Ensure name & price are included
    return JsonResponse(data, safe=False)

