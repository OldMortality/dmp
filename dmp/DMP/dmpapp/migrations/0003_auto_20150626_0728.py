# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmpapp', '0002_auto_20150605_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='description',
            field=models.CharField(default='description', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='id_copy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='access_permission',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='citations',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='coverage_end_date',
            field=models.DateField(null=True, verbose_name='coverage end date'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='coverage_space',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='coverage_start_date',
            field=models.DateField(null=True, verbose_name='coverage start date'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='end_date',
            field=models.DateField(null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='format',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='host_department',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='keywords',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='location',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='method_of_sharing',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='number_of_files',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='release_date',
            field=models.DateField(null=True, verbose_name='release date'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='retention_end_date',
            field=models.DateField(null=True, verbose_name='retention end date'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='space',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='start_date',
            field=models.DateField(null=True, verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='tools',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='ethics_document',
            name='approval_date',
            field=models.DateField(verbose_name='approval date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(null=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(null=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='funding_allocation',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='funding_source',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='research_code',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
    ]
