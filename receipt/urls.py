# pdf_app/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('generate-pdf/', pdf_view, name='generate_pdf'),
    path('generate-invoice/', transaction_view, name='generate_invoice'),
]
