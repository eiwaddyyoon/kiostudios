# Create your views here.
from django.views import generic
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
import logging

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

logger = logging.getLogger(__name__)

class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:index')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

# def index(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry" 
#             body = {
#             'name': form.cleaned_data['name'], 
#             'email_address': form.cleaned_data['email_address'],
#             'subject': form.cleaned_data['subject'],  
#             'message':form.cleaned_data['message'], 
#             }
#             message = "\n".join(body.values())

#             try:
#                 send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect ("portfolio:index")
    
#     form = ContactForm()
#     return render(request, "index.html", {'form':form})