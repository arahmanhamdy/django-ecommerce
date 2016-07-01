# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_so_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='so_no',
            field=models.CharField(default=orders.models.increment_order_number, max_length=64, null=True),
        ),
    ]
