# Generated by Django 3.0.6 on 2020-05-20 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0026_auto_20200514_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 12, 24, 49, 155825), verbose_name='Дата публикации'),
        ),
    ]
