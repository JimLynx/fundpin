from django.shortcuts import render

# Create your views here.
def index(request):
    """ return index page """
    return render(request, 'home/index.html')

def contact(request):
    """ return contact page """
    return render(request, 'home/contact.html')