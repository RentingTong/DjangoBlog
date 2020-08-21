"""
@date: 2020/08/19

@author: Tara

@description: Blog views.
"""
from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, template_name, context)