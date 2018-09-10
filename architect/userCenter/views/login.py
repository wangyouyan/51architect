# -*- coding:utf-8 -*-

from __future__ import division
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from userCenter.models import RegisterUserObject


def login_view(request):
    if request.method == 'GET':
        return render_to_response('users/login.html')
    elif request.method == 'POST':
        print(request.body)
        username = request.POST['username']
        password = request.POST['password']
        try:
            db_response = RegisterUserObject.objects.get(username=username)

        except Exception as login_error:
            return HttpResponse("当前你还未注册, 请点击注册页面进行注册!")

        finally:
            if password == db_response.password:
                return HttpResponseRedirect('/')
