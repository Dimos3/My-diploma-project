# Generated by Django 3.2.25 on 2024-05-25 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Artical', '0006_buyer_orders'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer_orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
