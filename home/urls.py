from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('job-postings/', views.job_postings, name='job-postings'),
    path('about/', views.about_us, name='about'),
]
