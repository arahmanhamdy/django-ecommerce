from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from products.models import Product
from .models import Order


def checkout(request):
    return render(request, "orders/checkout.html")


@login_required
def order(request):
    if request.method == "POST":
        item_count = int(request.POST.get('itemCount'))
        if not item_count:
            return redirect("orders:checkout")
        new_order = Order.objects.create(user_id=request.user)

        for i in range(1, item_count + 1):
            product_id = int(request.POST.get('item_id_%d' % i))
            product = get_object_or_404(Product, pk=product_id)
            order_line = {
                "product_id": product,
                "qty": request.POST.get('item_quantity_%d' % i),
                "unit_price": request.POST.get('item_price_%d' % i),
            }
            new_order.orderline_set.create(**order_line)
        return redirect('orders:view-order', new_order.id)
    else:
        return redirect('orders:checkout')


@login_required
def get_my_orders(request):
    orders = Order.objects.filter(user_id=request.user.id)
    return render(request, "orders/my-orders.html", {'orders': orders})


@login_required
def view_order(request, order_id):
    my_order = get_object_or_404(Order, pk=order_id)
    if my_order.user_id != request.user:
        raise PermissionDenied
    return render(request, "orders/view-order.html", {'order': my_order})
