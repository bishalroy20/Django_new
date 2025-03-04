from django import forms
from .models import addtask

class addForm(forms.ModelForm):
    class Meta:
        model = addtask
        fields = '__all__'
