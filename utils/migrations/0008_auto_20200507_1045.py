# Generated by Django 3.0.5 on 2020-05-07 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0007_auto_20200506_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 10, 45, 34, 465630), verbose_name='Дата публикации'),
        ),
    ]