# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmpapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmembers',
            name='person',
        ),
        migrations.RemoveField(
            model_name='projectmembers',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(related_name='project_member', to='dmpapp.Person'),
        ),
        migrations.DeleteModel(
            name='ProjectMembers',
        ),
    ]
