from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget= forms.TextInput(attrs={'id':'required'}),max_length=100)
    last_name = forms.CharField(widget= forms.TextInput(attrs={'id':'required'}),max_length=100)
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']
    

    
