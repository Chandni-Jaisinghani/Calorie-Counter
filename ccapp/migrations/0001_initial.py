# Generated by Django 3.2 on 2022-09-11 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('quantity', models.DecimalField(decimal_places=2, default=100.0, max_digits=7)),
                ('calories', models.IntegerField(default=0)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=7)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=7)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
