from django import forms
from .models import Organization

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone_number', 'email', 'role', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone_number', 'email', 'password1', 'password2']


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

