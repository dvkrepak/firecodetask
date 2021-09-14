# Generated by Django 3.2.7 on 2021-09-10 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.city', verbose_name='City')),
            ],
            options={
                'verbose_name': 'Street',
                'verbose_name_plural': 'Streets',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('number', models.IntegerField(verbose_name='Number')),
                ('opening_time', models.TimeField(verbose_name='Opening time')),
                ('closing_time', models.TimeField(verbose_name='Closing time')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.city', verbose_name='City')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.street', verbose_name='Street')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'ordering': ['id'],
            },
        ),
    ]