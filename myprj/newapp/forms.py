from django import forms
from .models import Tableone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Addform(forms.ModelForm):
    class Meta:
        model = Tableone
        fields = ['username', 'password', 'email']





class SignupForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'password1', 'password2', 'email']
