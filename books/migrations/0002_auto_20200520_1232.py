# Generated by Django 3.0.6 on 2020-05-20 09:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 12, 32, 35, 28551), verbose_name='Дата комментирования'),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('label_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.Label')),
            ],
            bases=('books.label',),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('label_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.Label')),
            ],
            bases=('books.label',),
        ),
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('label_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.Label')),
            ],
            bases=('books.label',),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(blank=True, to='books.Genre', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='books.Rating', verbose_name='Возрастной рейтинг'),
        ),
        migrations.AddField(
            model_name='book',
            name='warnings',
            field=models.ManyToManyField(blank=True, to='books.Warning', verbose_name='Предупреждения'),
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='genres',
            field=models.ManyToManyField(blank=True, to='books.Genre', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='books.Rating', verbose_name='Возрастной рейтинг'),
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='warnings',
            field=models.ManyToManyField(blank=True, to='books.Warning', verbose_name='Предупреждения'),
        ),
    ]
