from django.shortcuts import render

# Create your views here.
def view_cart(request):
    """ return donation cart page """
    return render(request, 'cart/cart.html')

