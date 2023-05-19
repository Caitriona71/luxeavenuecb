from django.db import models


# Create your models here.

class JobPosting(models.Model):
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    key_requirements = models.TextField()
    posted_date = models.DateField(auto_now_add=True)
    last_edit_date = models.DateField(auto_now=True)
    open = models.BooleanField(default=True)
