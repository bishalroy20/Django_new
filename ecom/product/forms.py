from django import forms 
from .models import Product , comment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name' , 'email' , 'body' ]