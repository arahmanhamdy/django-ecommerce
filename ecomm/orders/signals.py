import xmlrpclib
from django.conf import settings
from django.db import models
from .models import Order, OrderLine

DB, USER, PASSWORD = settings.ODOO_DATABASE, settings.ODOO_USER, settings.ODOO_PASSWORD


def get_uid_and_odoo_models():
    common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(settings.ODOO_URL))
    uid = common.authenticate(DB, USER, PASSWORD, {})
    odoo_models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(settings.ODOO_URL))
    return uid, odoo_models


def save_odoo_order(sender, instance, **kwargs):
    if kwargs.get("created"):
        uid, odoo_models = get_uid_and_odoo_models()
        search_partner_condition = [('ecomm_id', '=', instance.user_id.id)]
        odoo_partner_id = odoo_models.execute_kw(DB, uid, PASSWORD, 'res.partner', 'search',
                                                 [search_partner_condition])
        values = {
            "partner_id": odoo_partner_id[0],
            "ecomm_id": instance.id
        }
        new_id = odoo_models.execute_kw(DB, uid, PASSWORD, 'sale.order', 'create', [values])
        return new_id


def save_odoo_order_line(sender, instance, **kwargs):
    if kwargs.get("created"):
        uid, odoo_models = get_uid_and_odoo_models()
        values = {
            "description": instance.product_id.name,
            "product_uom_qty": instance.qty,
            "price_unit": instance.unit_price,
        }
        odoo_product_id = odoo_models.execute_kw(DB, uid, PASSWORD, 'product.product', 'search',
                                                  [[('ecomm_id', '=', instance.product_id.id)]])
        odoo_order_id = odoo_models.execute_kw(DB, uid, PASSWORD, 'sale.order', 'search',
                                                  [[('ecomm_id', '=', instance.order_id.id)]])
        values['order_id'] = odoo_order_id[0]
        values['product_id'] = odoo_product_id[0] if len(odoo_product_id) else False
        new_id = odoo_models.execute_kw(DB, uid, PASSWORD, 'sale.order.line', 'create', [values])
        return new_id


models.signals.post_save.connect(save_odoo_order, sender=Order)
models.signals.post_save.connect(save_odoo_order_line, sender=OrderLine)
