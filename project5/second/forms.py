from django import forms

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

