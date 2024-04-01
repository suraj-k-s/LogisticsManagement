# Generated by Django 5.0.3 on 2024-03-30 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_email', models.CharField(max_length=50)),
                ('admin_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_complainttype',
            fields=[
                ('complainttype_id', models.AutoField(primary_key=True, serialize=False)),
                ('complainttype_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_district',
            fields=[
                ('district_id', models.AutoField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_state',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_vehicletype',
            fields=[
                ('vehicletype_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicletype_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=50)),
                ('location_longitude', models.CharField(max_length=50)),
                ('location_latitude', models.CharField(max_length=50)),
                ('location_pincode', models.CharField(max_length=50)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_district')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_district',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_state'),
        ),
        migrations.CreateModel(
            name='tbl_vehiclesubtype',
            fields=[
                ('vehiclesubtype_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehiclesubtype_name', models.CharField(max_length=50)),
                ('vehicletype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_vehicletype')),
            ],
        ),
    ]
