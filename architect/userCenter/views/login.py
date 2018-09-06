# -*- coding:utf-8 -*-

from __future__ import division
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    login_response = authenticate(request, username=username, password=password)
    if login_response is not None:
        login(request, login_response)
        return HttpResponse("Congratulations,Login successful")
    else:
        return HttpResponse("incorrect username or password")
