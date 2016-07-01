from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from products.models import Product


def increment_order_number():
    prefix = 'SO'
    last_order = Order.objects.all().order_by('id').last()
    if not last_order:
        return prefix + '0001'
    so_no = last_order.so_no
    so_int = so_no.split(prefix)[-1]
    new_so_int = str(int(so_int) + 1).zfill(len(so_int))
    new_so_no = prefix + str(new_so_int)
    return new_so_no


@python_2_unicode_compatible
class Order(models.Model):
    so_no = models.CharField(max_length=64, default=increment_order_number, null=True)
    user_id = models.ForeignKey(User, verbose_name=_('user'))
    create_date = models.DateField(auto_now_add=True, verbose_name=_('order date'))

    def __str__(self):
        return self.so_no

    @property
    def total(self):
        return sum([line.unit_price * line.qty for line in self.orderline_set.all()])


class OrderLine(models.Model):
    product_id = models.ForeignKey(Product, verbose_name=_('product'))
    unit_price = models.FloatField(verbose_name=_('unit price'))
    qty = models.FloatField(verbose_name=_('Quantity'))
    order_id = models.ForeignKey(Order, verbose_name=_('category'))

    @property
    def total(self):
        return self.unit_price * self.qty
