# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmpapp', '0003_auto_20150626_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='id_copy',
        ),
    ]
