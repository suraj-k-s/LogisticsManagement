# Generated by Django 5.0.1 on 2024-03-31 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_vehicle',
            name='vehicle_status',
            field=models.IntegerField(default=0),
        ),
    ]
