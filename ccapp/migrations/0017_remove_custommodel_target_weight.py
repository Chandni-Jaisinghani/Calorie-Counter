# Generated by Django 3.2 on 2022-09-21 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0016_auto_20220920_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custommodel',
            name='target_weight',
        ),
    ]
