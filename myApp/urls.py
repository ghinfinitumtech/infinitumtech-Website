#myApp urls
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myApp.views import *

urlpatterns = [
    
    path('' , home, name='home'),
    path('about/', About, name="about"),
    path('services/<int:service_id>/', service_detail, name='service_detail'),
    path('careers_form/', careers_form, name='careers_form'),
    path('contact/',contact, name='contact'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
