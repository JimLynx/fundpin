from .views import blog_list, blog_description
from django.urls import path

urlpatterns = [
    path('', blog_list),
    path('<id>/', blog_description),
]
