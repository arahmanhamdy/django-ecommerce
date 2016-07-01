# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_product_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='order date')),
                ('user_id', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_price', models.FloatField(verbose_name='unit price')),
                ('qty', models.FloatField(verbose_name='Quantity')),
                ('order_id', models.ForeignKey(verbose_name='category', to='orders.Order')),
                ('product_id', models.ForeignKey(verbose_name='product', to='products.Product')),
            ],
        ),
    ]
