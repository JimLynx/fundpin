from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog'),
    path('<slug:slug>/', views.blog_description, name='blog_description'),
]
