#!/usr/bin/env python3
#
# Copyright (C) 2019 MST INC. All right reserved
#
# @file             : view.py
# @Create your views here.
# @檔案詳細描述, 內容包含哪些函式或類別, 實作了哪些功能,
# @author           : Ting
# @email            : wtyen17952@gmail.com
# @Date created     : 2019/12/12
# @last modified time: 2019/12/12
# @python version   : 3.6

from django.shortcuts import render
from django.shortcuts import render
from .models import Post
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    return render(request, 'index.html')


def about_mst(request):
    return render(request, 'about_mst.html')


def product(request):
    return render(request, 'product.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
#    a = str(request.POST.get['a', False])
#    b = str(request.POST.get['b', False])
#    c = str(request.POST.get['c', False])

    a = str(request.POST['a'])
    b = str(request.POST['b'])
    c = str(request.POST['c'])

#    try:
#        a = request.POST["a"]
#        b = request.POST["b"]
#        c = request.POST["c"]
#    except KeyError:
#        a = "False"
#        b = "False"
#        c = "False"

#    if 'a' in request.POST:
#        a = str(request.POST['a'])
#    else:
#        a = False


#    try:
#        a = request.POST['is_private']
#    except MultiValueDictKeyError:
#        a = "False"

#    create = Post.objects.create(title=a)

    create = Post.objects.create(title=a, location=b, content=c)

    return render(request, 'contact.html')

#    create = Post.objects.create(title=a)
#    b = str(request.GET['b'])

