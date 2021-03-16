from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from projects.models import Project


def view_cart(request):
    """ return donation cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add total donation selected to donation cart """

    project = get_object_or_404(Project, pk=item_id)
    donation_amount = int(request.POST.get('donation_amount'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = donation_amount

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """ remove item from donation cart """

    try:
        project = get_object_or_404(Project, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
