from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from projects.models import Project


def cart_contents(request):

    cart_items = []
    donation_amount = 0
    total = 0

    cart = request.session.get('cart', {})

    for item_id, donation_amount in cart.items():
        project = get_object_or_404(Project, pk=item_id)
        total += donation_amount
        cart_items.append({
            'item_id': item_id,
            'project': project,
            'donation_amount': donation_amount
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return context
