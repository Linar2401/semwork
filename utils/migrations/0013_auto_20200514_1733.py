# Generated by Django 3.0.6 on 2020-05-14 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0012_auto_20200507_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 17, 33, 38, 319262), verbose_name='Дата публикации'),
        ),
    ]
