from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(
            request, "Oops, there are no projects in your cart yet")
        return redirect(reverse('projects'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'stripe_public_key',
        'stripe_secret': 'stripe_secret',
    }

    return render(request, template, context)