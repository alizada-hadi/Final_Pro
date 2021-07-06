# Generated by Django 3.2.5 on 2021-07-06 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InterestTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('color', models.CharField(default='#007bff', max_length=14)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.category')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('kankor_id', models.CharField(max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('grand_father_name', models.CharField(max_length=200)),
                ('school_name', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=300)),
                ('province', models.CharField(max_length=200)),
                ('gender', models.CharField(default='male', max_length=20)),
                ('semester', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth')], default='First', max_length=20)),
                ('section', models.CharField(default='A', max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('hostle', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
                ('wing_number', models.IntegerField(default=1)),
                ('room_number', models.IntegerField(default=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('graduation_date_school', models.DateField(blank=True, null=True)),
                ('kankor_exam_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('chance', 'chance'), ('break', 'break'), ('nextYear', 'nextYear'), ('drop', 'drop')], default='active', max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('rel_with_std', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('phone1', models.CharField(max_length=200)),
                ('phone2', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('cart', models.CharField(blank=True, choices=[('electric', 'electric'), ('paper', 'paper')], default='electric', max_length=100, null=True)),
                ('cart_number', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('page_number', models.IntegerField(blank=True, null=True)),
                ('register_number', models.CharField(blank=True, max_length=200, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('cart_photo', models.ImageField(blank=True, null=True, upload_to='images/students/cart')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/students/avatar')),
                ('interests', models.ManyToManyField(related_name='interested_students', to='students.InterestTopic')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
            ],
        ),
    ]
