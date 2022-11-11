from django import forms
from django.core import validators
from django.contrib.auth.models import User
#class ChessForm(forms.Form):
    #location1=forms.CharField(min_length=2, max_length=2, strip=True)
    #location2=forms.CharField(min_length=2, max_length=2, strip=True)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'newpassword'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
        'username': None
        }

def validate_location(value):
    string1="abcdefgh"
    if (value[0] not in string1) or (not value[1].isdigit()):
        raise forms.ValidationError("Use format, e.g. e1.")
    if (int(value[1]) < 1 or int(value[1]) > 8):
        raise forms.ValidationError("Enter an integer from 1 to 8.")
