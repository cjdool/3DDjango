# Generated by Django 3.1.3 on 2020-11-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0002_auto_20201118_0230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='data status',
            new_name='data_status',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='date ended',
            new_name='date_ended',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='date requested',
            new_name='date_requested',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='date started',
            new_name='date_started',
        ),
    ]