"""
@date: 2020/08/19

@author: Tara

@description: Blog views.
"""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
