from django import forms 
from .models import authorModel

class authorForm(forms.ModelForm):
    class Meta:
        model = authorModel
        fields = '__all__'
