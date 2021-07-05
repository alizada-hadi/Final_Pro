# Generated by Django 3.2.5 on 2021-07-05 07:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('dep_status', models.CharField(choices=[('Lunched', 'Lunched'), ('Lunching', 'Lunching'), ('Not Available', 'Not Available')], default='Lunched', max_length=20)),
                ('dep_publish_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curr_code', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('curr', models.CharField(choices=[('Bachelor', 'Bachelor'), ('Master', 'Master')], default='Bachelor', max_length=20)),
                ('curr_name', models.CharField(max_length=200)),
                ('curr_credit', models.IntegerField()),
                ('curr_semester', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth')], default='First', max_length=20)),
                ('curr_type', models.CharField(choices=[('Main', 'Main'), ('Secondary', 'Secondary')], default='Main', max_length=50)),
                ('curr_description', ckeditor.fields.RichTextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='departments.department')),
            ],
        ),
    ]
