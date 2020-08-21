# -*- coding: utf-8 -*-
"""
@date: 2020/08/21

@author: Tara

@description: All forms of blog.
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
