from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        'project',
        'lineitem_total',
    )


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'total',
        'original_cart',
        'stripe_pid',
    )

    fields = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'street_address1',
        'street_address2',
        'county',
        'town_or_city',
        'postcode',
        'country',
        'date',
        'total',
        'original_cart',
        'stripe_pid',
    )

    list_display = (
        'order_number',
        'full_name',
        'date',
        'total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
