from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Project

def all_projects(request):
    """ A view to show all projects """

    projects = Project.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search item")
                return redirect(reverse('home'))
            
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            projects = projects.filter(queries)



    context = {
        'projects': projects,
        'search_term': query,
    }
    return render(request, 'projects/projects.html', context)


def project_description(request, project_id):
    """ A view to show individual projects """

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }
    return render(request, 'projects/project_description.html', context)
