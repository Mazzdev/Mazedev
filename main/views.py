from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render

from .forms import ContactForm


# Create your views here.

def home(request):
    return render(request, 'main/about.html', {'title': 'about'})


def portfolio(request):
    return render(request, 'main/portfolio.html', {'title': 'portfolio'})


def success2(request):
    return render(request, 'main/success2.html', {'title': 'Thanks for your message'})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['duldominik16@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'main/success2.html', {'title': 'Thanks for your message'})
    return render(request, "main/contact.html", {'form': form})
