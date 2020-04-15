from django import forms
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
    fullname=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your full name"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Your email id"}))
    content=forms.CharField(widget=forms.Textarea(attrs={ "placeholder":"send your query"}))


    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email must contain gmail.com")
        return email
