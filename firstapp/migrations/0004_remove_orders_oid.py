# Generated by Django 5.0.6 on 2024-05-24 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_orders_orderupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='oid',
        ),
    ]
