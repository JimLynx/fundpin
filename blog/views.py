from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_list(request):
    blog_list = Post.objects.all()
    context = {
        'blogs': blog_list,
    }
    return render(request, "blog/blog_list.html", context)


def blog_description(request, blog_id):
    blog_description = get_object_or_404(Post, pk=blog_id)
    context = {
        'blog_description': blog_description
    }
    return render(request, "blog/blog_description.html", context)
