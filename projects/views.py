from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Project, Category, Country
from .forms import ProjectForm


def all_projects(request):
    """ A view to show all projects, including search function"""

    projects = Project.objects.all()
    query = None
    categories = None
    countries = None
    sort = None
    direction = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            projects = projects.annotate(lower_name=Lower('name'))
        if sortkey == 'category':
            sortkey = 'category__name'
        if sortkey == 'country':
            sortkey = 'country__name'
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        projects = projects.order_by(sortkey)

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        projects = projects.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if 'country' in request.GET:
        countries = request.GET['country'].split(',')
        projects = projects.filter(country__name__in=countries)
        countries = Country.objects.filter(name__in=countries)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search item")
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            projects = projects.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'projects': projects,
        'search_term': query,
        'current_categories': categories,
        'current_countries': countries,
        'current_sorting': current_sorting,
    }

    return render(request, 'projects/projects.html', context)


def project_description(request, project_id):
    """ A view to show individual projects """

    project = get_object_or_404(Project, pk=project_id)

    context = {
        'project': project,
    }
    return render(request, 'projects/project_description.html', context)


def add_project(request):
    """ Add a new project """

    form = ProjectForm()
    template = 'projects/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
