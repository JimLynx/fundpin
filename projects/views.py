from django.shortcuts import render
from .models import Project

# Create your views here.
def all_projects(request):
    """ A view to show all projects """

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return render(request, 'projects/projects.html', context)
