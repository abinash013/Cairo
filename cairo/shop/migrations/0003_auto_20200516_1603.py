# Generated by Django 2.2.1 on 2020-05-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_department_department_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=2600),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
    ]
