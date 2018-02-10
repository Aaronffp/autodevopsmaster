# -*- coding:utf-8 -*-
# 
# File : jenkinsapi/views.py
# Author : 范丰平

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 创建服务状态接口，便于服务部署后，验证服务状态
def status(request):
    return HttpResponse(u'{\"status\":\"success\"}')

