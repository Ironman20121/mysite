# Generated by Django 2.1.5 on 2020-11-28 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201128_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 11, 6, 27, 793818), verbose_name='date published'),
        ),
    ]
