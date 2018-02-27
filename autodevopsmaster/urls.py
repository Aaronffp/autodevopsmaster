# -*- coding:utf-8 -*-
# 
# File : jenkinsapi/views.py
# Author : 范丰平

from sys import path_hooks

"""autodevopsmaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jenkinsapi import views as jenkinsapi_views
from pythondemo import views as demo_views

urlpatterns = [
    # jenkinsapi
    path('status', jenkinsapi_views.status),                           # 添加服务状态接口路由规则
    
    # pythondemo
    path('demo/comp', demo_views.comp),                                # Demo-001 : 获取请求参数
    path('demo/compd', demo_views.compd),                              # Demo-002 : 设置请求参数默认值
    path('demo/compr/<int:src>/<int:tar>', demo_views.compr),          # Demo-003 : RESTFUL API
    path('demo/home', demo_views.home),                                # Demo-004 : 服务首页(使用模板)
    path('demo/argstrans', demo_views.argstrans),                      # Demo-005 : 模板参数传递实例（一） --- 字符串实例
    path('demo/cycle', demo_views.cycle),                              # Demo-006 : 循环遍历实例
    
    path('admin/', admin.site.urls),
]


