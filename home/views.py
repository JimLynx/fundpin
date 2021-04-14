from django.shortcuts import render
from projects.models import Project
from blog.models import Post


def index(request):
    """ return index page """

    projects = Project.objects.all()
    blog = Post.objects.all()

    context = {
        'projects': projects,
        'blogs': blog
    }

    return render(request, 'home/index.html', context)


def contact(request):
    """ return contact page """

    return render(request, 'home/contact.html')
