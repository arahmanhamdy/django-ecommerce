from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def product_detail(request, product_id, *args):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, "products/product_detail.html", context)


def category_detail(request, category_id, *args):
    category = get_object_or_404(ProductCategory, pk=category_id)
    products_list = category.product_set.all()
    paginator = Paginator(products_list, 10)
    page = request.GET.get('page')
    try:
        products_list = paginator.page(page)
    except PageNotAnInteger:
        products_list = paginator.page(1)
    except EmptyPage:
        products_list = paginator.page(paginator.num_pages)
    context = {
        'category_name': category.name,
        'products': products_list,
        'pages': range(1, paginator.num_pages + 1)
    }
    return render(request, "products/category_detail.html", context)