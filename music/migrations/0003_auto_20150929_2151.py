# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20150929_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=set([]),
        ),
    ]
