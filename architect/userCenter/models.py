
# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.
"""
        "form-first-name=wangyouyan&form-last-name=15611703075&form-email=wangyouyan%40aliyun.com&form-email=abcd-1234&form-email=abcd-1234"
"""


class RegisterUserObject(models.Model):
    id = models.CharField(max_length=80,primary_key=True,verbose_name=u'ID')
    username = models.CharField(max_length=20,blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    cellphone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=20,blank=True,null=True)
    is_activate = models.BooleanField(default=False)
    comment = models.CharField(max_length=20,blank=True,null=True)
    class Meta():
        verbose_name_plural = u"用户注册信息"
        db_table = 'register_user'
