# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=120)
    #dob = models.DateField(auto_now=False, auto_now_add = False)
    #contact = models.BigIntegerField()


    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        #return "/blogs/%s/" %(self.id)
        return reverse("info:user_detail", kwargs = {"id":self.id})
