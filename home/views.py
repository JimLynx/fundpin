from django.shortcuts import render
from projects.models import Project


def index(request):
    """ return index page """

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'home/index.html', context)


def contact(request):
    """ return contact page """
    return render(request, 'home/contact.html')
