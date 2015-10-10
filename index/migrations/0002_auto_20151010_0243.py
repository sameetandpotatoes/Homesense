# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='group',
            field=models.ForeignKey(to='index.Group', db_column=b'groupID'),
        ),
    ]
