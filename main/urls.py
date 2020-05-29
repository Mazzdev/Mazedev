from django.urls import path
from .views import home, portfolio, contact

urlpatterns = [
    path('', home),
    path('portfolio', portfolio),
    path('contact', contact),
]