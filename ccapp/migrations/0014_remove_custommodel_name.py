# Generated by Django 3.2 on 2022-09-18 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0013_custommodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custommodel',
            name='name',
        ),
    ]
