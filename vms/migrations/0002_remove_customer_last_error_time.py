# Generated by Django 2.0.2 on 2018-05-10 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='last_error_time',
        ),
    ]
