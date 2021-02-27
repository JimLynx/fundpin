from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_projects, name='projects'),
    path('<project_id>', views.project_description, name='project_description'),
]