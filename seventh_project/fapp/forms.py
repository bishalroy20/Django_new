from django import forms
from fapp.models import studentmodel

class studentform(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields = '__all__'
        # labels = {
        #     'name' : 'Student name'
        # }
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class': 'btn-primary'})
            
        # }
        