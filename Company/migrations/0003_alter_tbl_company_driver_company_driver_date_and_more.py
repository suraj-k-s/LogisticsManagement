# Generated by Django 5.0.1 on 2024-03-31 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_alter_tbl_vehicle_vehicle_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_company_driver',
            name='company_driver_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tbl_driver_request',
            name='request_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tbl_transport_shedule',
            name='transport_shedule_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
