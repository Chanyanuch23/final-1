from django import forms 
from django.forms.fields import EmailField 
from django.forms.widgets import Textarea 
# sfrom django.contrib.auth.forms import UserCreateFrom #

class LoginForm(forms.Form): 
   Username = forms.CharField(max_length=100) 
   Password = forms.CharField(max_length=100)
   
class RegForm(forms.Form):
   Username = forms.CharField(max_length=100) 
   Email = forms.EmailField()
   Password = forms.CharField(max_length=100)

# #
# class CustomerRegistrationFrom(UserCreateFrom):
#    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'from-control'}))
#    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'from-control'}))
#    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'from-control'}))
#    password2 = forms.CharField(label='Confirm',widget=forms.PasswordInput(attrs={'class':'from-control'}))
#