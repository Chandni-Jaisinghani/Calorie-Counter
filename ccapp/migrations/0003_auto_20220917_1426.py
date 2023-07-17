# Generated by Django 3.2 on 2022-09-17 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0002_auto_20220917_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custommodel',
            old_name='cweight',
            new_name='currentweight',
        ),
        migrations.RenameField(
            model_name='custommodel',
            old_name='activity',
            new_name='dailyactivity',
        ),
        migrations.RenameField(
            model_name='custommodel',
            old_name='medical',
            new_name='medicalconditions',
        ),
        migrations.RenameField(
            model_name='custommodel',
            old_name='tweight',
            new_name='targetweight',
        ),
        migrations.AddField(
            model_name='custommodel',
            name='gender',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
