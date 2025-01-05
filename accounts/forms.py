from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from .models import CustomUser

class UserCreationFormCustom(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email",)

class UserChangeFormCustom(UserChangeForm):
    class Meta:
        model=CustomUser
        fields = ("username", "first_name", "last_name", "email",)