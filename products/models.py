# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from ecommerce.utils import unique_slug_generator
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length = 120)
    slug        = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    image       = models.ImageField(upload_to='products/', null=True, blank=True)
    price       = models.DecimalField(decimal_places = 3, max_digits = 20)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def get_absolute_urls(self):
        #return "/products/{slug}".format(slug=self.slug)
        return reverse("products:detail", kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
