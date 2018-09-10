
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponse, Http404
import urllib
from django.core.mail import send_mail
from django.conf import settings as django_settings


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render_to_response('homepage/index.html')

def contact_us(request):
    if request.method == 'POST':
        request_data = request.body
        if isinstance(request.body, bytes):
            request_data = request.body.encode('utf-8')
        url_request_data = urllib.unquote(request.body)
        data_template = url_request_data.split('&')
        data_dict = {}
        if isinstance(data_template, list):
            for li in data_template:
                k = li.split('=')[0]
                v = li.split('=')[1]
                data_dict[k] = v
        try:
            send_mail(data_dict['subject'], data_dict['message'], django_settings.EMAIL_HOST_USER, ['wangyouyan201314@163.com'],
                      fail_silently=False)
            send_mail('意见反馈', '尊敬的用户， 51架构师网已收到您的意见反馈!您的宝贵意见， 我们将虚心接受。',
                      django_settings.EMAIL_HOST_USER, [data_dict['email']], fail_silently=False)
        except IndexError:
            return Http404

        return HttpResponse('We have received your email')

def login_views(request):
    if request.method == 'GET':
        return render_to_response('login.html')

def register_views(request):
    if request.method == 'GET':
        return render_to_response('users/register.html')
    elif request.method == 'POST':
        print(request.body)
        """username=wyyservice&phone-number=15611703075&email=wangyouyan%40aliyun.com&first-input=abcd-1234&repeat-password=abcd-1234
        """
        request_data = request.body
        if isinstance(request.body, bytes):
            request_data = request.body.encode('utf-8')
        url_request_data = urllib.unquote(request.body)
        data_template = url_request_data.split('&')
        data_dict = {}
        if isinstance(data_template, list):
            for li in data_template:
                k = li.split('=')[0]
                v = li.split('=')[1]
                data_dict[k] = v
        if data_dict['first-input'] == data_dict['repeat-password']:
            subject = "51架构师网用户注册通知"
            message = "亲爱的%s, 感谢你注册51架构师网!请点击以下链接进行账户激活。" % data_dict['username']
            send_mail(subject, message, django_settings.EMAIL_HOST_USER, [data_dict['email']],
                      fail_silently=False)
        else:
            return HttpResponse('两次输入的密码不一致,请重新确认!')
        return HttpResponse('恭喜您注册成功!')
