from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_projects, name='projects'),
    path('<int:project_id>/', views.project_description, name='project_description'),
    path('add/', views.add_project, name='add_project'),
    path('edit/<int:project_id>/', views.edit_project, name='edit_project'),
]