from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from .forms import CommentForm


def blog_list(request):
    """ return blog list page """

    blog_list = Post.objects.all()

    template = 'blog/blog_list.html'
    context = {
        'blogs': blog_list,
    }

    return render(request, template, context)


def blog_description(request, slug):
    """ return blog description page for each blog """

    blog_description = get_object_or_404(Post, slug=slug)
    comments = blog_description.comments.filter(active=True).order_by("-created_on")
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog_description
            new_comment.save()
    else:
        comment_form = CommentForm()

    template = 'blog/blog_description.html'
    context = {
        'blog_description': blog_description,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, template, context)
