# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20151010_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='code',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='group',
            name='code',
            field=models.CharField(max_length=200),
        ),
    ]
