# from .views import blog_list, blog_description
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog'),
    path('<int:blog_id>/', views.blog_description, name='blog_description'),
]
