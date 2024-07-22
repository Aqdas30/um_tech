# Assuming the contact and services models are in the 'contact' and 'services' apps respectively

from django.contrib import admin

from mainApp.models import Contact, Service

admin.site.register(Service)
admin.site.register(Contact)