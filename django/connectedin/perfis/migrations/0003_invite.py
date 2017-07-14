# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_perfil_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('invited', models.ForeignKey(related_name='invite_received', to='perfis.Perfil')),
                ('requester', models.ForeignKey(related_name='invite_sent', to='perfis.Perfil')),
            ],
        ),
    ]
