# Generated by Django 4.0.6 on 2022-08-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(blank=True, max_length=255, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
                ('provincia', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_id', models.TextField(blank=True, null=True)),
                ('employee_id', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposCliente',
            fields=[
                ('tipoid', models.AutoField(db_column='tipoId', primary_key=True, serialize=False)),
                ('plan_cliente', models.TextField()),
            ],
            options={
                'db_table': 'tipos_cliente',
                'managed': False,
            },
        ),
    ]
