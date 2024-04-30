from django.shortcuts import render
from myApp.models import *
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from myApp.forms import *
# views.py
from django.shortcuts import render, redirect
from .forms import CareerApplicationForm
from django.contrib import messages


# Create your views here.

def home(request):
    banner = Banner.objects.all()
    testiomial=Testimonials.objects.all()
    team_mb=TeamMembers.objects.all()
    # details=CompanyDetails.objects.get(pk=1)
    return render(request, 'myApp/home.html', locals())

def About(request):
    return render(request, 'myApp/about.html')

def service_detail(request, service_id):
    service_id = get_object_or_404(Services, pk=service_id)
    # details=CompanyDetails.objects.get(pk=1)
    return render(request, 'myApp/service_detail.html',  locals())


def careers_form(request):
    if request.method == 'POST':
        form = CareerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Display success message
            messages.success(request, 'Your form has been submitted successfully.')
            # Redirect to the success page or another view
            return redirect('careers_form')  # Redirect to the same page (GET request)
    else:
        # If it's a GET request or the form is not valid, render an empty form
        form = CareerApplicationForm()
    return render(request, 'myApp/careers_form.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Display success message
            messages.success(request, 'Your form has been submitted successfully.')
            # Redirect to a success page or another view
            return redirect('contact')  # Redirect to the same page (GET request)
        else:
            # If form is invalid, display error messages
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'myApp/contact.html', {'form': form})