from django.shortcuts import render
from django.shortcuts import HttpResponse
from listings.models import Band
from listings.models import Listing

# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/hello.html',
                     {'bands': bands}
                  )

def about(request):
    return render(request, 
                  'listings/about.html'
                  )

def listings(request):
    listings = Listing.objects.all()
    return render(request, 
                  'listings/listings.html',
                     {'listings': listings}
                  )

def contact(request):
    return render(request, 
                  'listings/contact.html'
                  )