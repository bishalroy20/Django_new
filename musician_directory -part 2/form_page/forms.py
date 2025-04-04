from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import authorModel

class authorForm(forms.ModelForm):
    class Meta:
        model = authorModel
        fields = '__all__'


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name','email']

class changeuserdata(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name','email']