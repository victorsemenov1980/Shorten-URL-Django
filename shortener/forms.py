#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:10:37 2020

@author: user
"""


from django import forms
from .models import url

class UrlForm(forms.Form):
    url = forms.URLField(label='URL',)
    hash_ = forms.CharField(label='Hash value - optional', max_length=15,required=False,)
    
    