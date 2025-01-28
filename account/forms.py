from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser

class SignUpForm(UserCreationForm):
    display_name = forms.CharField(max_length=150, required=True, help_text='Please enter your name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'display_name', 'email', 'password1', 'password2', )