"""
@date: 2020/08/18

@author: Tara

@description: Blog models.
"""
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     comment_title = models.CharField(max_length=200)
#     comment_content = models.CharField(max_length=2000)
#     post_date = models.DateTimeField('post date')
#
#     def __str__(self):
#         return self.comment_title

