# Generated by Django 3.2.5 on 2021-07-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210714_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='slug',
            field=models.SlugField(),
        ),
    ]