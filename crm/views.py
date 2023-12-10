from django.shortcuts import render
from models import Order


def first_page(request):
    return render(request, './index.html')
# Create your views here.
