# -*- coding:utf-8 -*-
# 
# File : jenkinsapi/views.py
# Author : 范丰平

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Demo-001 : 获取请求参数
def comp(request):
    src = int(request.GET['src'])
    tar = int(request.GET['tar'])
    
    if src > tar :
        msg = str(src) + ' > ' + str(tar)
    elif src == tar :
        msg = str(src) + ' = ' + str(tar)
    else:
        msg = str(src) + ' < ' + str(tar)
    
    return HttpResponse(msg)
