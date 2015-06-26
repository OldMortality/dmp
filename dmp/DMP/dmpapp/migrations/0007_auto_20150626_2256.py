# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dmpapp', '0006_auto_20150626_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='access_permission',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='citations',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='coverage_end_date',
            field=models.DateField(verbose_name='coverage end date', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='coverage_space',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='coverage_start_date',
            field=models.DateField(verbose_name='coverage start date', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, to='dmpapp.Person', related_name='ds_creator'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='description',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='end_date',
            field=models.DateField(verbose_name='end date', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='format',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='host_department',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='keywords',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='location',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='method_of_sharing',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='number_of_files',
            field=models.IntegerField(null=True, default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, to='dmpapp.Person', related_name='ds_owner'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='release_date',
            field=models.DateField(verbose_name='release date', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='retention_end_date',
            field=models.DateField(verbose_name='retention end date', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='space',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='start_date',
            field=models.DateField(verbose_name='start date', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='tools',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(null=True, max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(verbose_name='end date', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='funding_allocation',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='funding_source',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='research_code',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='start date', null=True, blank=True),
        ),
    ]
