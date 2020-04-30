from PIL import Image
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model


class GuestForm(forms.Form):
    email = forms.EmailField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


User= get_user_model()
class RegisterForm(forms.Form):
    username  = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email     = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    img       = forms.ImageField()
    password  = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'class':"form-control"}))


    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already exist")
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exist")
        return email

    def clean(self):
        data      = self.cleaned_data
        username  = self.cleaned_data.get('username')
        email     = self.cleaned_data.get('email')
        password  = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("passwords must match")
        return data
