# Generated by Django 3.2.5 on 2021-07-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_visited_at'),
        ('events', '0002_event_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='course',
        ),
        migrations.AddField(
            model_name='event',
            name='course',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]