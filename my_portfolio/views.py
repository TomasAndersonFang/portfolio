#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 21:28
# @Author  : Tomas Anderson Fang
# @Email   : fasunkonw@gmail.com
# @File    : views.py
# @Software: PyCharm

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

