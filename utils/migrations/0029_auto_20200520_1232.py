# Generated by Django 3.0.6 on 2020-05-20 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0028_auto_20200520_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 12, 32, 35, 23551), verbose_name='Дата публикации'),
        ),
    ]
