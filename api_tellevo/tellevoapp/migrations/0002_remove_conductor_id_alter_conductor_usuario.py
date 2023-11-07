# Generated by Django 4.2.5 on 2023-11-07 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tellevoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conductor',
            name='id',
        ),
        migrations.AlterField(
            model_name='conductor',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
