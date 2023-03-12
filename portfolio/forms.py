from django import forms
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=30)
    email_address = forms.EmailField(label='')
    subject = forms.CharField(label='', max_length=30)
    message = forms.CharField(label='', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control mt-3'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'

        self.fields['email_address'].widget.attrs['class'] = 'form-control mt-3'
        self.fields['email_address'].widget.attrs['placeholder'] = 'Email Address'

        self.fields['subject'].widget.attrs['class'] = 'form-control mt-3'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'

        self.fields['message'].widget.attrs['class'] = 'form-control mb-3 mt-3'
        self.fields['message'].widget.attrs['placeholder'] = 'Message Details'
       

    def send_email(self):
        name = self.cleaned_data['name']
        email_address = self.cleaned_data['email_address']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        message = 'Sender Name: {0}\nMail Address: {1}\nSubject: {2}\nMessage: {3}\n'.format(name, email_address, subject, message)
        from_email = email_address
        to_list = [
            'admin@example.com'
        ]
        cc_list = [
            ''
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()