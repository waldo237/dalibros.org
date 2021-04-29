from django.shortcuts import render

# Create your views here.
from .models import Donation, Book, Author, Donor, Receiver, Gender

# show description


def index(request):
    return render(request, 'store/index.html')
