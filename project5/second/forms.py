from django import forms
from django.core import validators

class contactform(forms.Form):
    name = forms.CharField(label = "username" , initial="BISHAL ROY" ,required=True ,disabled=False , help_text="Total length must be within 20 words" ) # , widget=forms.Textarea(attrs = {'id' : 'textarea' , 'class' : 'class1'}) 
    # file = forms.FileField()
    # image = forms.ImageField()
    email = forms.EmailField( label = "email")
    # age = forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput())
    # weight = forms.FloatField()
    weight = forms.CharField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    # birthday = forms.DateField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date' }))
    # appointment = forms.DateTimeField()
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local' }))
    c=[('s' , 'small'),('m' , 'medium'),('h' ,'hard')]
    # size = forms.ChoiceField(choices=c)
    size = forms.ChoiceField(choices=c , widget=forms.RadioSelect)
    d = [('p' , 'paperoni') , ('c' , 'chiken') , ('m' , 'mashroom')]
    # pizza = forms.MultipleChoiceField(choices=d)
    pizza = forms.MultipleChoiceField(choices=d , widget=forms.CheckboxSelectMultiple)


# class studentform(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("must be at least 10 char")
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("must be a valid email")
    #     return valemail

    # def clean(self):
    #     cleand_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("must be at least 10 char")

    #     if '.com' not in valemail:
    #         raise forms.ValidationError("must be a valid email")


class studentform(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5 , message = 'enter a name at least 5 char')])
    email = forms.CharField(widget=forms.EmailInput , validators=[validators.EmailValidator(message = 'enter a valid email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35 , message='under 34 age') ,validators.MinValueValidator(18 , message ='at least 18 to show')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'] , message='file extension is not correct')])

class password_validation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password= forms.CharField(widget=forms.PasswordInput)
    con_pass = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['con_pass']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("password doesnot match")
        if len(val_name) <5:
            raise forms.ValidationError("must be at least 5 char")