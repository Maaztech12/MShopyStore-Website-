# Generated by Django 5.0.6 on 2024-05-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_remove_orders_oid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='paymentstatus',
            field=models.CharField(blank=True, default='PAID', max_length=20),
        ),
    ]