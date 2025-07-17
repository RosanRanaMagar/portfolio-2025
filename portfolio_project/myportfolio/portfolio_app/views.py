# portfolio_app/views.py
from django.shortcuts import render
from .models import Project
from .forms import ContactForm

def home(request):
    return render(request, 'portfolio_app/home.html')

def about(request):
    return render(request, 'portfolio_app/about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/projects.html', {'projects': projects})


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Manually save data to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data.get('phone', ''),
                message=form.cleaned_data['message']
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Redirect to prevent duplicate submissions
    else:
        form = ContactForm()

    return render(request, 'portfolio_app/contact.html', {'form': form}) 
    
"""
    
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage
from .utils import send_sms_notification  # Import your SMS function

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data.get('phone', ''),
                message=form.cleaned_data['message']
            )

            # Send SMS Notification
            sms_status = send_sms_notification(contact_message)
            if sms_status:
                messages.success(request, "Your message has been sent, and the admin has been notified via SMS!")
            else:
                messages.warning(request, "Your message was sent, but SMS notification failed.")

            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'portfolio_app/contact.html', {'form': form}) """
  
  
from django.urls import reverse
from django.http import HttpResponseRedirect
from .send_sms import sendsms
from .models import ContactMessage
from django.utils import timezone
from .forms import ContactForm
from .send_sms import sendsms


def send_view(request):
    if request.method == "POST":
        fom = ContactForm(request.POST)
        if fom.is_valid():
            name=fom.cleaned_data['name'],
            email=fom.cleaned_data['email'],
            subject=fom.cleaned_data['subject'],
            phone=fom.cleaned_data.get('phone', ''),
            message=fom.cleaned_data['message']
            created_at = timezone.now()
            contact_obj = ContactMessage(name=name, email=email, subject=subject, phone=phone, message=message, created_at=created_at)
            contact_obj.save()
            sendsms()
            
            return HttpResponseRedirect(reverse('success_page'))
    else:
        fom = ContactForm()
        data = {'fom':fom}
        return render(request, 'portfolio_app/contact.html', data)
    
def success_view(request):
    return render(request, 'portfolio_app/success.html')