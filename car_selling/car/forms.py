from django import forms 
from .models import Car , comment

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name' , 'email' , 'body' ]