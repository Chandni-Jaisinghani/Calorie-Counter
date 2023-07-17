# Generated by Django 3.2 on 2022-09-18 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ccapp', '0010_custommodel_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='custommodel',
            name='usr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]