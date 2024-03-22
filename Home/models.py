
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings

class vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    register_no=models.CharField(max_length=100)
    makers_class=models.CharField(max_length=100)
    vehicle_class=models.CharField(max_length=100)
    fuel=models.CharField(max_length=100)
    engine=models.CharField(max_length=100)
    insurance=models.CharField(max_length=100)
    def __str__(self):
            return self. register_no



class bin_color(models.Model):
    bin_color=models.CharField(max_length=100)
    bin_type=models.CharField(max_length=100)
    def __str__(self):
            return self.bin_color


class location(models.Model):
    region = models.CharField(max_length=100)
    def __str__(self):
            return self.region
class scheduleingday(models.Model):
    region = models.ForeignKey(location,verbose_name='region',on_delete=models.DO_NOTHING,default="")
    schedule_id = models.AutoField(primary_key=True)
    direction = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    def __str__(self):
        return self.day


class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="")
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    driver_address = models.CharField(max_length=200)
    driver_email = models.CharField(max_length=100, unique=True)
    driver_phone = models.BigIntegerField()
    driver_licence = models.CharField(max_length=100)
    driver_vehicle = models.ForeignKey(vehicle, verbose_name='register_no', on_delete=models.DO_NOTHING,default="")
    driver_location = models.ForeignKey(location, verbose_name=' region', on_delete=models.DO_NOTHING,default="")
    driver_image = models.ImageField()
    def __str__(self):
            return self.name
class Bins(models.Model):
    Bin_id = models.AutoField(primary_key=True)
    Bin_name = models.CharField(max_length=100)
    Bin_color = models.ForeignKey(bin_color, verbose_name='bin_color', on_delete=models.DO_NOTHING, default="")
    Bin_location = models.ForeignKey(location, verbose_name='region', on_delete=models.DO_NOTHING, default="")
    Bin_address1 = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    # distance_KM = models.CharField(max_length=100)
    # total_time = models.TimeField(default=0)
    # Bin_date= models.DateField(default=0)
    Bin_status = models.CharField(max_length=50)
    collections_day = models.ForeignKey(scheduleingday,verbose_name='day',on_delete=models.DO_NOTHING,default="")
    allocated_driver = models.ForeignKey(Driver, verbose_name='Allocated Driver', on_delete=models.DO_NOTHING)

    def __str__(self):
            return self.Bin_name


class complaintpost(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    complaint_id = models.AutoField(primary_key=True)
    c_landmark = models.CharField(max_length=100)
    bin = models.ForeignKey(Bins, on_delete=models.CASCADE)
    c_complant = models.TextField(max_length=500)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.c_landmark
    













