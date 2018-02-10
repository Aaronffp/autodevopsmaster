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

# Demo-002 : 设置请求参数默认值
def compd(request):
    src = int(request.GET['src'])
    tar = int(request.GET.get('tar', 2019))
    
    if src > tar :
        msg = str(src) + ' > ' + str(tar)
    elif src == tar :
        msg = str(src) + ' = ' + str(tar)
    else:
        msg = str(src) + ' < ' + str(tar)
    
    return HttpResponse(msg)

# Demo-003 : RESTFUL API
def compr(request, src, tar):
    src = int(src)
    tar = int(tar)
    
    if src > tar :
        msg = str(src) + ' > ' + str(tar)
    elif src == tar :
        msg = str(src) + ' = ' + str(tar)
    else:
        msg = str(src) + ' < ' + str(tar)
    
    return HttpResponse(msg)

# Demo-004 : 创建首页信息(使用模板)
def home(request):
    return render(request, 'home.html')



