# -*- coding: utf-8 -*-
"""
@date: 2020/08/06

@author: Tara

@description:
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]