# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='job',
            field=models.CharField(default='undefined', max_length=255),
        ),
    ]
