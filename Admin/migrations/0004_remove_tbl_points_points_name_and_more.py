# Generated by Django 5.0.1 on 2024-04-27 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_remove_tbl_route_from_location_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_points',
            name='points_name',
        ),
        migrations.AddField(
            model_name='tbl_route',
            name='from_location_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_routes', to='Admin.tbl_location'),
        ),
        migrations.AddField(
            model_name='tbl_route',
            name='route_distance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='tbl_route',
            name='to_location_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_routes', to='Admin.tbl_location'),
        ),
        migrations.AlterField(
            model_name='tbl_points',
            name='points_distance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
