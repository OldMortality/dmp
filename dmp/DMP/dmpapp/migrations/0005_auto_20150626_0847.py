# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmpapp', '0004_remove_project_id_copy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='creator',
            field=models.ForeignKey(related_name='ds_creator', null=True, to='dmpapp.Person'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='owner',
            field=models.ForeignKey(related_name='ds_owner', null=True, to='dmpapp.Person'),
        ),
    ]
