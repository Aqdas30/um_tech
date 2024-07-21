from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

from django.shortcuts import render, redirect
from .forms import ContactForm

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# def index(request):
#     if request.method == 'POST' and 'contact_form' in request.POST:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone_number = form.cleaned_data['phone_number']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             service_type = form.cleaned_data['service_type']

#             send_mail(
#                 subject=f'Contact Form Submission from {name}',
#                 message=f'Phone Number: {phone_number}\nEmail: {email}\nService Type: {service_type}\nMessage: {message}',
#                 from_email=email,
#                 recipient_list=[settings.CONTACT_EMAIL],
#                 fail_silently=False,
#             )
            
#             # Redirect to the same page with a success message
#             return render(request, 'index.html', {
#                 'form': form,
#                 'success_message': 'Your message has been sent successfully!'
#             })
#     else:
#         form = ContactForm()

#     return render(request, 'index.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            service_type = form.cleaned_data['service_type']

            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=f'Phone Number: {phone_number}\nEmail: {email}\nService Type: {service_type}\nMessage: {message}',
                from_email=email,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            # Redirect to the same page or a success page
            return redirect('index')  # Redirect to the index view or another view if needed
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone_number = form.cleaned_data['phone_number']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             service_type = form.cleaned_data['service_type']

#             send_mail(
#                 subject=f'Contact Form Submission from {name}',
#                 message=f'Phone Number: {phone_number}\nEmail: {email}\nService Type: {service_type}\nMessage: {message}',
#                 from_email=email,
#                 recipient_list=[settings.CONTACT_EMAIL],
#                 fail_silently=False,
#             )
            
#             return redirect('contact_success')
#     else:
#         form = ContactForm()

#     return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceListPreviewView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.all()[:3]

      