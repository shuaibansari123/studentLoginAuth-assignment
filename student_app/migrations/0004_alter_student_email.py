# Generated by Django 5.0.6 on 2024-08-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_alter_student_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
