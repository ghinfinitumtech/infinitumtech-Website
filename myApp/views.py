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
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            date = form.cleaned_data.get('date')
            resume = request.FILES.get('resume')
            gender = form.cleaned_data.get('gender', '') 
            address = form.cleaned_data.get('address')

            career_application = CareerApplication(
                name=name, email=email, phone=phone,
                date=date, address=address, resume=resume, gender=gender
            )
            
            career_application.save()

            message=messages.success(request, 'Your form has been submitted successfully.')
            
            # Redirect to the success page or another view
            return redirect('careers_form')  

    else:
        form = CareerApplicationForm()

    return render(request, 'myApp/careers_form.html', {'form': form})




def contact(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            subject = form.cleaned_data.get('subject', '') 
            message = form.cleaned_data.get('message')

            print(name, email, phone, subject, message)

            career_application = Contact(
                name=name, email=email, phone=phone,
                subject=subject, message=message
            )

            career_application.save()

            messages.success(request, 'Your form has been submitted successfully.')

            # Redirect to the success page or another view
            return redirect('contact')

    else:
        form = Contact_Form()

    return render(request, 'myApp/contact.html', {'form': form})
