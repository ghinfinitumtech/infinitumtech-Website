from django.contrib import admin
from myApp.models import *

# Register your models here.

admin.site.register(Banner)
admin.site.register(Technologie)
admin.site.register(Project)
admin.site.register(Services)
admin.site.register(Testimonials)
admin.site.register(TeamMembers)
admin.site.register(CareerApplication)
admin.site.register(Contact)


@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow adding only if there are no instances of CompanyDetails
        return not CompanyDetails.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of CompanyDetails instance
        return False
