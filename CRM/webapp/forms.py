from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms
from django.forms.widgets import PasswordInput, TextInput

#registration
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Login
class LoginForm(AuthenticationForm) :

    username = forms.CharField(max_length=30, widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#create a record
class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ["first_name", "last_name",'email','phone','state','city','country']

#update a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone','state','city','country']

#edit a record


           

        	
                   