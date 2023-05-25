from django.contrib import admin
from .models import JobPosting, StaffMember, StoreLocation


# Register your models here.
class JobPostingAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'job_description',
        'key_requirements',
        'posted_date',
        'last_edit_date',
        'open',
    )

    ordering = ('job_title',)


admin.site.register(JobPosting, JobPostingAdmin)


class StaffMemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'job_title',
        'bio',
        'photo',
    )

    ordering = ('name',)


admin.site.register(StaffMember, StaffMemberAdmin)


class StoreLocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'phone',
        'photo',
    )

    ordering = ('name',)


admin.site.register(StoreLocation, StoreLocationAdmin)
