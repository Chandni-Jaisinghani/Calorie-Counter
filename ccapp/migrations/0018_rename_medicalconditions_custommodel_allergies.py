# Generated by Django 3.2 on 2022-09-21 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0017_remove_custommodel_target_weight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custommodel',
            old_name='medicalconditions',
            new_name='allergies',
        ),
    ]
