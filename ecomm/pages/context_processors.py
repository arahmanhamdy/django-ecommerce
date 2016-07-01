from django.conf import settings
from products.models import ProductCategory


def layout_processor(request):
    categories_list = ProductCategory.objects.all()
    # divide categories into 3 partitions
    n = 3
    categories_length = len(categories_list)
    if categories_length % n == 2:
        p = (categories_length / n) + 1
    else:
        p = categories_length / n
    categories = []
    last = 0
    for i in range(n - 1):
        categories.append(categories_list[p * i: p * (i + 1)])
        last = i
    # push the last partition to the end of the list
    categories.append(categories_list[p * (last + 1):])
    return {
        'categories': categories,
        'site_name': settings.SITE_NAME
    }
