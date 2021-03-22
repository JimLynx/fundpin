from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_info = intent.charges.data[0].billing_info
        total = round(intent.data.charges[0].amount / 100, 2)

        order_exists = False
        try:
            order = Order.object.get(
                full_name__iexact=billing_info.name,
                email__iexact=billing_info.email,
                phone_number__iexact=billing_info.phone,
                country__iexact=billing_info.country,
                postcode__iexact=billing_info.postal_code,
                town_or_city__iexact=billing_info.city,
                street_address1__iexact=billing_info.line1,
                street_address2__iexact=billing_info.line2,
                county__iexact=billing_info.state,
                total__iexact=billing_info.total,
            )
            order_exists = True

            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    full_name=billing_info.name,
                    email=billing_info.email,
                    phone_number=billing_info.phone,
                    country=billing_info.country,
                    postcode=billing_info.postal_code,
                    town_or_city=billing_info.city,
                    street_address1=billing_info.line1,
                    street_address2=billing_info.line2,
                    county=billing_info.state,
                )
                for item_id, item_data in json.loads(cart).items():
                    project = Project.objects.get(id=item_id)
                    donation_amount = Decimal(item_data)

                    order_line_item = OrderLineItem(
                        order=order,
                        project=project,
                        lineitem_total=donation_amount,
                    )
                    order_line_item.save()
                    order_line_item.order.total += order_line_item.lineitem_total
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.failed webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
