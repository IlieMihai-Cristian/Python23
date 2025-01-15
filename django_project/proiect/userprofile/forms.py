from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'Email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
        }
