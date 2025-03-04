from django import forms
from .models import add_category

class category_Form(forms.ModelForm):
    class Meta:
        model = add_category
        fields = '__all__'
