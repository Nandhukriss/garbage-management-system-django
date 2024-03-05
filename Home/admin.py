from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import vehicle,bin_color,Bins,location,Driver, complaintpost,workupdation,scheduleingday
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
# admin.site.register(Bins)
# admin.site.register(vehicle)
# admin.site.register(employee)
admin.site.register(bin_color)
admin.site.register(location)
# admin.site.register(Driver)
admin.site.register(complaintpost)
admin.site.register(workupdation)
# admin.site.register(scheduleingday)
def export_bin(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Bins.csv"'
    writer = csv.writer(response)
    writer.writerow(['Bin Name','Bin color','Bin Address1','Bin Address2 ','Bin Address3', 'Zip code'])
    registration = queryset.values_list('Bin_name','Bin_color','Bin_address1','Bin_address2','Bin_address3','pincode')
    for i in registration:
        writer.writerow(i)
    return response


export_bin.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['Bin_name','Bin_color','Bin_address1','Bin_address2','Bin_address3','pincode']
    actions = [export_bin]
admin.site.register(Bins,RegAdmin)


def export_driver(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Driver.csv"'
    writer = csv.writer(response)
    writer.writerow(['Driver Name','Driver Address','Email ','Phone', 'Licence NO'])
    registration = queryset.values_list('name','driver_address','driver_email','driver_phone','driver_licence')
    for i in registration:
        writer.writerow(i)
    return response


export_driver.short_description = 'Export to csv'


# class RegAdmin(admin.ModelAdmin):
#     list_display = ['name','driver_address','driver_email','driver_phone','driver_licence']
#     actions = [export_driver]
# admin.site.register(Driver,RegAdmin)
class RegAdmin(admin.ModelAdmin):
    list_display = ['name', 'driver_address', 'driver_email', 'driver_phone', 'driver_licence']
    actions = [export_driver]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = get_user_model().objects.filter(is_driverreg=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Driver, RegAdmin)



def export_Day(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Day.csv"'
    writer = csv.writer(response)
    writer.writerow(['Region','Direction','Day'])
    registration = queryset.values_list('region','direction','day')
    for i in registration:
        writer.writerow(i)
    return response


export_Day.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['region','direction','day']
    actions = [export_Day]
admin.site.register(scheduleingday,RegAdmin)



def export_vehicle(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vehicle.csv"'
    writer = csv.writer(response)
    writer.writerow(['Registered No','Registered Owner','Registered Address','Makers Class', 'Vehicle Class','Engine','Insurance'])
    registration = queryset.values_list('register_no','regd_owner','reg_address','makers_class','vehicle_class','engine','insurance')
    for i in registration:
        writer.writerow(i)
    return response


export_vehicle.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['register_no','regd_owner','reg_address','makers_class','vehicle_class','engine','insurance']
    actions = [export_vehicle]
admin.site.register(vehicle,RegAdmin)

# Register your models here.
