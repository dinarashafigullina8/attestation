# Generated by Django 4.2.3 on 2023-08-02 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230725_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='phone',
        ),
        migrations.AddField(
            model_name='phone',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='core.company', verbose_name='Компания'),
            preserve_default=False,
        ),
    ]
