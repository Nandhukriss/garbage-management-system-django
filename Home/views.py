from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Bins,complaintpost,Driver
def home(request):
    return render(request, 'index.html')
def registration(request):
    return render(request, 'registration.html')
def registration1(request):
    return render(request, 'registration1.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'services.html')


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
            return redirect('post-complaint') 

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


def driver_complaints(request):
    """
    This function retrieves all the complaints that are  a driver.

    Parameters:
        request (HttpRequest): The current request object

    Returns:
        HttpResponse: A response object with the rendered template
    """
    current_user = request.user

    # Fetch the driver object associated with the current user
    driver = Driver.objects.get(user=current_user)

    # Fetch all bins related to the current driver
    driver_bins = driver.bins_set.all()

    # Fetch all complaints related to the bins of the current driver
    driver_complaints = complaintpost.objects.filter(bin__in=driver_bins).order_by('-complaint_id')

    return render(request, 'view_assigned_complaints.html', {'driver_complaints': driver_complaints})

def mark_complaint_done(request, complaint_id):
    if request.method == 'POST':
        complaint = complaintpost.objects.get(complaint_id=complaint_id)
        complaint.status = True
        complaint.save()
        return redirect('view_assigned_complaints')
def mark_complaint_undone(request, complaint_id):
    if request.method == 'POST':
        complaint = complaintpost.objects.get(complaint_id=complaint_id)
        complaint.status = False
        complaint.save()
        return redirect('view_assigned_complaints')
