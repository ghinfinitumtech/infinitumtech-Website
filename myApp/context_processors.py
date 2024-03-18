from .models import CompanyDetails,Services

def company_details(request):
    details=CompanyDetails.objects.first()
    service = Services.objects.all()
    return {"details":details,"service":service}

