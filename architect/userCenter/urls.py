# -*- coding:utf-8 -*-

from __future__ import division

from django.conf.urls import include, url
from userCenter.views.login import login_view
from userCenter.views.logout import logout_view
from userCenter.views.register import regiester_view
from userCenter.views.reset_password import reset_password_view

urlpatterns = [
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^register$', regiester_view, name='register'),
    url(r'^reset_password$', reset_password_view, name='reset_password'),
]

