# Generated by Django 3.2.5 on 2021-07-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_alter_curriculumuploadlist_date_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='slug',
            field=models.SlugField(default='computer-science-1', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
