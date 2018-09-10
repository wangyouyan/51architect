
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponse, Http404
import urllib
from django.core.mail import send_mail
from django.conf import settings as django_settings


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render_to_response('index.html')


def contact_us(request):
    if request.method == 'POST':
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
        try:
            send_mail(data_dict['subject'], data_dict['message'], django_settings.EMAIL_HOST_USER,
                      ['wangyouyan@aliyun.com'],
                      fail_silently=False)
            send_mail('意见反馈', '尊敬的用户， 51架构师网已收到您的意见反馈!您的宝贵意见， 我们将虚心接受。',
                      django_settings.EMAIL_HOST_USER, [data_dict['email']], fail_silently=False)
        except IndexError:
            return Http404

        return HttpResponse('We have received your email')
