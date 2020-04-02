from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm

import datetime


def home_page(request):
    return render(request,"home_page.html",{})

def contact_page(request):
    contact_form = ContactForm()
    print(request.POST.get('fullname'))
    context={
     'form' : contact_form
    }
    return render(request, 'contact/view.html',context)

def about_page(request):
    return render(request, 'home_page.html',{})
