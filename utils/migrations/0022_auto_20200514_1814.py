# Generated by Django 3.0.6 on 2020-05-14 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0021_auto_20200514_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 18, 14, 29, 255703), verbose_name='Дата публикации'),
        ),
    ]
