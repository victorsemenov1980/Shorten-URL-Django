#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:48:22 2020

@author: user
"""



from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('result',views.result,name='result'),
    path('<link>',views.go,name='go')
]
