# -*- coding: utf-8 -*-
"""
@date: 2020/08/17

@author: Tara

@description: Url patterns.

"""
from django.urls import path
from . import views


# app_name = "blog"

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]
