# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('tools', models.CharField(max_length=30)),
                ('coverage_start_date', models.DateTimeField(verbose_name='coverage start date')),
                ('coverage_end_date', models.DateTimeField(verbose_name='coverage end date')),
                ('coverage_space', models.CharField(max_length=30)),
                ('format', models.CharField(max_length=30)),
                ('keywords', models.CharField(max_length=30)),
                ('citations', models.CharField(max_length=30)),
                ('host_department', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('number_of_files', models.IntegerField(default=0)),
                ('space', models.CharField(max_length=30)),
                ('retention_end_date', models.DateTimeField(verbose_name='retention end date')),
                ('release_date', models.DateTimeField(verbose_name='release date')),
                ('access_permission', models.CharField(max_length=30)),
                ('method_of_sharing', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ethics_Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('approval_number', models.CharField(max_length=30)),
                ('consenting_body', models.CharField(max_length=30)),
                ('approval_date', models.DateTimeField(verbose_name='approval date')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('description', models.CharField(max_length=100)),
                ('funding_source', models.CharField(max_length=100)),
                ('funding_allocation', models.CharField(max_length=30)),
                ('research_code', models.CharField(max_length=30)),
                ('principal', models.ForeignKey(to='dmpapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMembers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('person', models.ForeignKey(to='dmpapp.Person')),
                ('project', models.ForeignKey(to='dmpapp.Project')),
            ],
        ),
        migrations.AddField(
            model_name='ethics_document',
            name='project',
            field=models.ForeignKey(to='dmpapp.Project'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='creator',
            field=models.ForeignKey(related_name='ds_creator', to='dmpapp.Person'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='owner',
            field=models.ForeignKey(related_name='ds_owner', to='dmpapp.Person'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='project',
            field=models.ForeignKey(to='dmpapp.Project'),
        ),
    ]
