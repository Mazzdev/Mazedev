from django.urls import path
from .views import home, portfolio, contact, success2

urlpatterns = [
    path('', home),
    path('portfolio', portfolio),
    path('contact', contact),
    path('success2', success2),
]
