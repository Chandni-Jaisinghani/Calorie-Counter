# Generated by Django 3.2 on 2022-09-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0020_auto_20220921_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewplanmodel',
            name='mid_snck_options',
        ),
        migrations.AddField(
            model_name='viewplanmodel',
            name='mid_snack_options',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='avoid_such_foods',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='bmi',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='breakfast_options',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='dinner_options',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='food_intake',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='lunch_options',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='tips',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='total_carbs',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='total_fats',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewplanmodel',
            name='total_protein',
            field=models.CharField(max_length=100),
        ),
    ]
