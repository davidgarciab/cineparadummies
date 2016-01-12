# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('rate', models.DecimalField(max_digits=1, decimal_places=1, blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(to='review.Film'),
        ),
    ]
