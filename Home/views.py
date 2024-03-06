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


def Views_bin(request):

    driver = Driver.objects.filter(user=request.user)  

    # Get the allocated bins associated with the driver
    # viewbin = driver.Allocatted_bin.all()
    viewbin = Bins.objects.filter()

    return render(request,"see.html",{'Bins':viewbin})

def complaint(request):
    if request.method == 'POST':
        landmark = request.POST.get('c_landmark')
        bin_number = request.POST.get('bin_number')
        complaint_text = request.POST.get('c_complaint')


        try:
            # Convert the bin_number to an integer and retrieve the corresponding Bins instance
            bin_instance = Bins.objects.get(Bin_id=int(bin_number))
        except Bins.DoesNotExist:
            messages.error(request, 'Invalid Bin selected')
            return redirect('your_failure_page')  # Change 'your_failure_page' to your actual failure page

        # Create a new complaint
        new_complaint = complaintpost.objects.create(
            name=request.user,
            c_landmark=landmark,
            bin=bin_instance,
            c_complant=complaint_text
        )

    # Fetch all available bins for the dropdown
    all_bins = Bins.objects.all()

    return render(request, 'complaint.html', {'available_bins': all_bins})

    
def view_all_complaints(request):
    complaints = complaintpost.objects.filter(name=request.user)
    return render(request, 'view_all_complaints.html', {'complaints': complaints})


# @login_required(login_url='login')  # Redirect to login page if not logged in

def driver_complaints(request):
    # Get the current user (assuming the user is a driver)
    current_user = request.user.driver

    # Fetch all complaints related to the current driver
    driver_complaints = workupdation.objects.filter(name=current_user).order_by('-Date', '-Time')

    return render(request, 'view_assigned_complaints.html', {'driver_complaints': driver_complaints})

