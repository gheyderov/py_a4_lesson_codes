from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'email',
            'subject',
            'message'
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your name'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Your email'
            }),
            'subject' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Subject'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Message'
            })
        }
    
    # def clean(self):
    #     value = self.cleaned_data['email']
    #     if not value.endswith('@gmail.com'):
    #         raise forms.ValidationError('Email must be ended with gmail.com')
    #     return value
    
    def clean_email(self):
        value = self.cleaned_data['email']
        if not value.endswith('@gmail.com'):
            raise forms.ValidationError('Email must be ended with gmail.com')
        return value
    
    def clean_first_name(self):
        value = self.cleaned_data['first_name']
        return value.lower()