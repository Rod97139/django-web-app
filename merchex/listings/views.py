from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail

# Create your views here.

def band_list(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/band_list.html',
                     {'bands': bands}
                  )

def band_detail(request, id):
    band = Band.objects.get(id=id)  
    return render(request,
          'listings/band_detail.html',
          {'band': band})

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

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, 
                  'listings/listing_detail.html',
                     {'listing': listing}
                  )

def contact(request):
    if request.method == 'POST':
    # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('email-sent')  
            
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
          'listings/contact.html',
          {'form': form})  

def email_sent(request):
    return render(request,
          'listings/email_sent.html')