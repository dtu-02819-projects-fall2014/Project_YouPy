# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('videoid', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
