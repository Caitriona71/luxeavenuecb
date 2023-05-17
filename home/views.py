from django.shortcuts import render

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
    return render(request, 'about_us.html, context')