# Generated by Django 4.1.13 on 2024-03-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Econtact',
            field=models.PositiveSmallIntegerField(max_length=10),
        ),
    ]
