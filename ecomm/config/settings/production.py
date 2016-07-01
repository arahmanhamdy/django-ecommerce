from .base import *

# Turn off DEBUG on production
DEBUG = False
ALLOWED_HOSTS = ['seechic.os34.tech']
STATIC_ROOT = '/var/www/html/seechic.os34.tech/static/'
MEDIA_ROOT = '/var/www/html/seechic.os34.tech/media/'

# odoo integration
ODOO_URL = "http://odoo.os34.tech"
