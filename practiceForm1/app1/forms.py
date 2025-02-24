from django import forms 
from django.forms.widgets import NumberInput 
import datetime
from .models import SModel


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class practiceform(forms.Form):
    name = forms.CharField(max_length=10)
    roll_number = forms.IntegerField( help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())  
    email = forms.EmailField(label="Please enter your email address",required=False)
    # comment1 = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField(initial=False)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(initial =datetime.date.today ,widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)



class practicemodelform(forms.ModelForm):
    class Meta:
        model = SModel
        fields = "__all__"
        