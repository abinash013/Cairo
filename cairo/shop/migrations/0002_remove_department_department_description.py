# Generated by Django 2.2.1 on 2020-05-16 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='department_description',
        ),
    ]
