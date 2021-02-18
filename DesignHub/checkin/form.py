from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm, fields
from .models import visitor

class VisitorForm(ModelForm):
    class Meta:
        model = visitor
        fields ="__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


