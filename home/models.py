from django.db import models


# Create your models here.

class JobPosting(models.Model):
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    key_requirements = models.TextField()
    posted_date = models.DateField(auto_now_add=True)
    last_edit_date = models.DateField(auto_now=True)
    open = models.BooleanField(default=True)


class StaffMember(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='photos/')


class StoreLocation(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/')