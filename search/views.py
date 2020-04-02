# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db.models import Q
from django.views.generic import ListView

from products.models import Product

from django.shortcuts import render

# Create your views here.

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
            request     = self.request
            method_dict = request.GET
            query       = method_dict.get('q', None) #method_dict['q']
            if query is not None:
                lookup = (
                           Q(title__icontains=query) |
                           Q(description__icontains=query) | 
                           Q(price__icontains=query)
                          )
                return Product.objects.filter(lookup).distinct()  #Product.objects.filter(title__iexact=query)
            return Product.objects.none()
