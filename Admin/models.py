from django.db import models

class tbl_admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_email = models.CharField(max_length=50)
    admin_password = models.CharField(max_length=50)

class tbl_category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)


class tbl_complainttype(models.Model):
    complainttype_id = models.AutoField(primary_key=True)
    complainttype_name = models.CharField(max_length=50)



class tbl_state(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)



class tbl_district(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=50)
    state_id = models.ForeignKey(tbl_state,on_delete=models.CASCADE)


class tbl_location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    district_id = models.ForeignKey(tbl_district,on_delete=models.CASCADE)


class tbl_route(models.Model):
    route_id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=50)
    from_location_id = models.ForeignKey(tbl_location, on_delete=models.CASCADE, related_name="from_routes",null=True)
    to_location_id = models.ForeignKey(tbl_location, on_delete=models.CASCADE, related_name="to_routes",null=True)
    route_distance = models.DecimalField(max_digits=10, decimal_places=2,null=True) 



class tbl_points(models.Model):
    points_id = models.AutoField(primary_key=True)
    points_distance = models.DecimalField(max_digits=10, decimal_places=2)  
    points_order = models.CharField(max_length=50)
    location_id = models.ForeignKey(tbl_location,on_delete=models.CASCADE,null=True)
    route_id = models.ForeignKey(tbl_route,on_delete=models.CASCADE)


class tbl_vehicletype(models.Model):
    vehicletype_id = models.AutoField(primary_key=True)
    vehicletype_name = models.CharField(max_length=50)



class tbl_vehiclesubtype(models.Model):
    vehiclesubtype_id = models.AutoField(primary_key=True)
    vehiclesubtype_name = models.CharField(max_length=50)
    vehicletype_id = models.ForeignKey(tbl_vehicletype,on_delete=models.CASCADE)
