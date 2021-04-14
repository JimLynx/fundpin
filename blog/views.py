from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_list(request):
    """ return blog list page """

    blog_list = Post.objects.all()

    template = 'blog/blog_list.html'
    context = {
        'blogs': blog_list,
    }

    return render(request, template, context)


def blog_description(request, slug):
    """ return index pageblog description page for each blog """

    blog_description = get_object_or_404(Post, slug=slug)

    template = 'blog/blog_description.html'
    context = {
        'blog_description': blog_description
    }
    return render(request, template, context)
