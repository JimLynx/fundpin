from .views import blog_list
from django.urls import path

urlpatterns = [
    path('', blog_list),
]
