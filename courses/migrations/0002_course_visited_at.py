# Generated by Django 3.2.5 on 2021-07-08 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='visited_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
