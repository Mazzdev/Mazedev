from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/about.html', {'title': 'about'})

def portfolio(request):
    return render(request, 'main/portfolio.html', {'title': 'portfolio'})

def contact(request):
    return render(request, 'main/contact.html', {'title': 'contact'})