# portfolio_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact_view, name='contact'),
    path('send_sms/', views.send_view, name='send_sms'),  # Send SMS page
    path('success/', views.success_view, name='success_page'),  # Success page


]
