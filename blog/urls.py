from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<slug:slug>/', views.edit_blog, name='edit_blog'),
    path('<slug:slug>/', views.blog_description, name='blog_description'),
]
