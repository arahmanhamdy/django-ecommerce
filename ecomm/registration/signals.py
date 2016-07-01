import xmlrpclib
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


def save_odoo_customer(sender, instance, **kwargs):
    if kwargs.get("created"):
        db, user, password = settings.ODOO_DATABASE, settings.ODOO_USER, settings.ODOO_PASSWORD
        common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(settings.ODOO_URL))
        uid = common.authenticate(db, user, password, {})
        odoo_models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(settings.ODOO_URL))
        values = {
            "name": instance.username,
            "customer": True,
            "email": instance.email,
            "ecomm_id": instance.id
        }
        new_id = odoo_models.execute_kw(db, uid, password, 'res.partner', 'create', [values])
        return new_id


models.signals.post_save.connect(save_odoo_customer, sender=User)
