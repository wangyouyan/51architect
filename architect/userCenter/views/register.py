# -*- coding:utf-8 -*-

from __future__ import division
from django.shortcuts import render_to_response, HttpResponse
import urllib
from django.core.mail import send_mail
from django.conf import settings as django_settings
from userCenter.models import RegisterUserObject
import random_object_id.random_object_id as random_object_id


def regiester_view(request):
    if request.method == 'GET':
        return render_to_response('users/register.html')
    elif request.method == 'POST':
        request_data = request.body
        if isinstance(request.body, bytes):
            request_data = request.body.encode('utf-8')
        url_request_data = urllib.unquote(request_data)
        data_template = url_request_data.split('&')
        data_dict = {}
        if isinstance(data_template, list):
            for li in data_template:
                k = li.split('=')[0]
                v = li.split('=')[1]
                data_dict[k] = v
        if data_dict['password'] == data_dict['repeat-password']:
            register_data = RegisterUserObject(id=random_object_id.gen_random_object_id(),
                                               username=data_dict['username'], password=data_dict['password'],
                                               cellphone=data_dict['cellphone'], email=data_dict['email'])
            register_data.save()
            subject = "51架构师网用户注册通知"
            message = "亲爱的%s, 感谢你注册51架构师网!请点击以下链接进行账户激活。" % data_dict['username']
            send_mail(subject, message, django_settings.EMAIL_HOST_USER, [data_dict['email']],
                      fail_silently=False)
        else:
            return HttpResponse('两次输入的密码不一致,请重新确认!')
        return HttpResponse('恭喜您注册成功!')
