# Generated by Django 4.1 on 2022-08-26 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_alter_profile_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='customer_id',
        ),
    ]
