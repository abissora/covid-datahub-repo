from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

# class UserRegisterForm for create user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

# class UserUpdateForm for user update
class UserUpdateForm(forms.ModelForm):
            email = forms.EmailField()

            class Meta:
                model = User
                fields = ['username', 'email']

# class ProfileUpdateForm for user profile update
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


