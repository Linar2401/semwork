# Generated by Django 3.0.6 on 2020-05-14 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0023_auto_20200514_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 18, 16, 53, 536340), verbose_name='Дата публикации'),
        ),
    ]
