# Generated by Django 5.0.1 on 2024-04-04 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0003_rename_transport_update_location_tbl_transport_update_transport_update_latitude_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_transport_update',
        ),
    ]
