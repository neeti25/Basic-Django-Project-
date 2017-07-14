# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import UserInfo
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def user_list(request):
    queryset = UserInfo.objects.all()
    context = {
    "object_list": queryset,
    "title": "User Information",
    }
    return render(request, "list.html", context)


def user_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "form":form,
    }
    return render(request, "form.html", context)


def user_edit(request,id=None):
    instance = get_object_or_404(UserInfo, id = id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title":instance.first_name,
        "instance" : instance,
        "form":form,
    }
    return render(request, "form.html", context)


def user_delete(request,id = None):
    instance = get_object_or_404(UserInfo, id = id)
    instance.delete()
    return redirect('info:user_list')


def user_detail(request, id):
    instance = get_object_or_404(UserInfo, id = id)
    context = {
        "title":"User Detail",
        "instance" : instance,
    }
    return render(request, "detail.html", context)
