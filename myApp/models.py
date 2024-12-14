from typing import Any
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name


class Technologie(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="technology", null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="projects", null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    git_hub = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    live = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100)
    banner_image = models.ImageField(
        upload_to="services/banner", default="img/banner/page-title.jpg"
    )
    image = models.ImageField(upload_to="services/mages")
    icons = models.ImageField(upload_to="services/mages/logos", null=True, blank=True)
    content = models.CharField(max_length=80)
    descriptions = models.TextField(max_length=1000)
    technology = models.ForeignKey(
        Technologie, on_delete=models.CASCADE, null=True, blank=True
    )
    projects = models.ManyToManyField(Project, blank=True, null=True)
    main_services = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Testimonials/")
    designation = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name


class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team/")
    designation = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class CareerApplication(models.Model):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    phone = models.IntegerField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class CompanyDetails(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="Company/")
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = PhoneNumberField(null=False, blank=False)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
