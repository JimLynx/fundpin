from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from projects.models import Project


def cart_contents(request):

    cart_items = []
    total = 0
    donation_amount = 0 #amount submitted from project description form

    cart = request.session.get('cart', {})

    context = {
        'cart_items': cart_items,
        'total': total,
        'donation_amount': donation_amount,
    }

    return context