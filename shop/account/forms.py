from django import forms
from models import Account

class RegistrationForm(forms.ModelForm):    
    class Meta:
        model = Account
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, min_length=6)