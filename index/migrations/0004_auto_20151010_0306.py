# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20151010_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='sensorType',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='sensor',
            name='zipCode',
            field=models.CharField(default=b'', max_length=5),
        ),
    ]
