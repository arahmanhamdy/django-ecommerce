import xmlrpclib
from django.conf import settings
from django.db import models
from .models import Product, ProductCategory

DB, USER, PASSWORD = settings.ODOO_DATABASE, settings.ODOO_USER, settings.ODOO_PASSWORD


def get_uid_and_odoo_models():
    common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(settings.ODOO_URL))
    uid = common.authenticate(DB, USER, PASSWORD, {})
    odoo_models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(settings.ODOO_URL))
    return uid, odoo_models


def save_odoo_product_category(sender, instance, **kwargs):
    if kwargs.get("created"):
        uid, odoo_models = get_uid_and_odoo_models()
        values = {
            "name": instance.name,
            "ecomm_id": instance.id
        }
        new_id = odoo_models.execute_kw(DB, uid, PASSWORD, 'product.category', 'create', [values])
        return new_id


def save_odoo_product(sender, instance, **kwargs):
    if kwargs.get("created"):
        uid, odoo_models = get_uid_and_odoo_models()
        values = {
            "name": instance.name,
            "description": instance.description,
            "list_price": instance.price,
            "ecomm_id": instance.id,
        }
        odoo_category_id = odoo_models.execute_kw(DB, uid, PASSWORD, 'product.category', 'search',
                                        [[('ecomm_id', '=', instance.category_id.id)]])
        values['categ_id'] = odoo_category_id[0]
        new_id = odoo_models.execute_kw(DB, uid, PASSWORD, 'product.product', 'create', [values])
        return new_id


models.signals.post_save.connect(save_odoo_product_category, sender=ProductCategory)
models.signals.post_save.connect(save_odoo_product, sender=Product)
