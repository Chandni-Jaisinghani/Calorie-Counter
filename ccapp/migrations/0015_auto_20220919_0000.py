# Generated by Django 3.2 on 2022-09-18 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ccapp', '0014_remove_custommodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewplanmodel',
            name='name',
        ),
        migrations.AddField(
            model_name='viewplanmodel',
            name='usr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
