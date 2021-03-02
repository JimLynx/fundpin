from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from projects.models import Project


def cart_contents(request):

    cart_items = []
    total = 0
    project_count = 0

    cart = request.session.get('cart', {})

    context = {
        'cart_items': cart_items,
        'total': total,
        'project_count': project_count,
    }

    return context