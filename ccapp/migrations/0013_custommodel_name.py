# Generated by Django 3.2 on 2022-09-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0012_remove_custommodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='custommodel',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]