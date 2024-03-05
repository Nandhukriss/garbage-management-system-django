from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Bins,complaintpost,Driver,workupdation
def hom(request):
    return render(request, 'index.html')
def registration(request):
    return render(request, 'registration.html')
def registration1(request):
    return render(request, 'registration1.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def base(request):
    return render(request, 'base.html')
def service(request):
    return render(request, 'services.html')
def home1(request):
    return render(request, 'home1.html')

def driverregistration(request):
    return render(request, 'driverreg.html')
# def complaint(request):
#     return render(request,'complaint.html')



def Views_bin(request):
    viewbin = Bins.objects.all()

    return render(request,"see.html",{'Bins':viewbin})

def complaint(request):
    if request.method == 'POST':

        landmark = request.POST.get('c_landmark')
        bin_number = request.POST.get('bin_number')
        complaint_text = request.POST.get('c_complaint')

        # Create a new complaint
        new_complaint = complaintpost.objects.create(
            name=request.user,  # Assuming the user is authenticated
            c_landmark=landmark,
            bin_number=bin_number,
            c_complant=complaint_text
        )

        # Identify the relevant bin and location
        bin = Bins.objects.get(Bin_id=new_complaint.bin_number)
        location = bin.Bin_location

        # Find available drivers for the location and scheduling day
        available_drivers = Driver.objects.filter(
            driver_location=location,
            Allocatted_bin=None  # Assuming drivers with no allocated bin are available
        )

        if available_drivers.exists():
            # Notify the first available driver
            selected_driver = available_drivers.first()

            # Assign the complaint to the driver
            selected_driver.Allocatted_bin = bin
            selected_driver.save()

            # Acknowledge the complaint
            # Update the workupdation model with the driver's acknowledgment
            workupdation.objects.create(
                Bin_id=bin,
                Location=location,
                Time=None,  # You can set the time when the driver acknowledges
                Date=None,  # You can set the date when the driver acknowledges
                status="Acknowledged",
                Driver_name=selected_driver
            )

            # Redirect or display a success message
            return redirect('success_page')  # Change 'success_page' to your actual success page
        else:
            # Handle the case when no available drivers are found
            messages.error(request, 'Invalid Credentials')  # Create a template for this case

    # Render the form for posting complaints
    return render(request, 'complaint.html')

    
def view_all_complaints(request):
    complaints = complaintpost.objects.filter(name=request.user)
    return render(request, 'view_all_complaints.html', {'complaints': complaints})

# @login_required(login_url='login')  # Redirect to login page if not logged in
def view_assigned_complaints(request):
    driver = Driver.objects.filter(user=request.user).first()
    assigned_complaints = workupdation.objects.filter(name=driver).values('Bin_id__Bin_name', 'Location__region', 'Time', 'Date', 'status', 'Bin_id__collections_day__day', 'Bin_id__Bin_color__bin_color', 'Bin_id__Bin_location__region').order_by('-Date', '-Time')


    return render(request, 'view_assigned_complaints.html', {'assigned_complaints': assigned_complaints})

# def searchbar(request):
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query:
#             Bin_name = Bins.objects.filter(Bin_name__icontains=query)
#             return render(request, 'searchresult.html', {'Bin_name':Bin_name})
#         else:
#             print("No information to show")
#             return render(request, 'searchbar.html', {})

# def searchresult(request):
#     return render(searchresult,'searchresult.html')
