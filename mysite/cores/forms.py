from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,  help_text='Optional.')
    last_name = forms.CharField(max_length=30,  help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    address = forms.CharField(max_length=500)
    pin = forms.IntegerField()
    aadhar = forms.IntegerField()
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'birth_date','address','pin','aadhar', 'password1', 'password2', )
