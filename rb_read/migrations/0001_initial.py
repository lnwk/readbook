# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rb_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='readInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rchapter', models.CharField(max_length=200)),
                ('rneirong', tinymce.models.HTMLField()),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rb_books.booksInfo')),
            ],
        ),
    ]
