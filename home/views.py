from django.shortcuts import render
from .models import JobPosting, StaffMember, StoreLocation

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about_us(request):
    staff_members = StaffMember.objects.all()
    store_locations = StoreLocation.objects.all()

    context = {
        'staff_members': staff_members,
        'store_locations': store_locations
    }
    return render(request, 'home/about.html', context)


def store_locations(request):
    store_locations = StoreLocation.objects.all()

    context = {
        'store_locations': store_locations,
    }
    return render(request, 'home/store-locations.html', context)


def job_postings(request):
    job_postings = JobPosting.objects.filter(open=True)

    context = {
        'job_postings': job_postings,
    }
    return render(request, 'home/job-postings.html', context)