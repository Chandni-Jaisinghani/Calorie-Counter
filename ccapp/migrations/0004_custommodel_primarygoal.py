# Generated by Django 3.2 on 2022-09-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0003_auto_20220917_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='custommodel',
            name='primarygoal',
            field=models.CharField(default=2, max_length=40),
            preserve_default=False,
        ),
    ]
