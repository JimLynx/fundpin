from django.shortcuts import render
from .models import Post


def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list': post
    }
    return render(request, "blog/blog_list.html", context)


def blog_description(request, id):
    per_post = Post.objects.get(id=id)
    context = {
        'blog_description': per_post
    }
    return render(request, "blog/blog_description.html", context)
