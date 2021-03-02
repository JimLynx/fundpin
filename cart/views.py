from django.shortcuts import render, redirect


def view_cart(request):
    """ return donation cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add total donation selecrted to donation cart """

    donation_amount = int(request.POST.get('donation_amount'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id] = donation_amount

    request.session['cart'] = cart

    print(request.session['cart'])
    return redirect(redirect_url)