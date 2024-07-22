from django import forms
from .models import Service

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    service_type = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['service_type'].choices = [(service.id, service.title) for service in Service.objects.all()]
