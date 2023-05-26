from django.db import models

# Create your models here.

class Band(models.Model):
    name = models.fields.CharField(max_length=100)

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)


# >>> from listings.models import Listing
#     listing = Listing()
# >>> listing.name = 'Cut Copy'
# >>> listing.save()
# >>> listing
# listing = Listing.objects.create(title='Beethoven - Sonate au clair de lune - manuscrit original EXTRÊMEMENT RARE')