from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from variables.models import Location




class Country(models.Model):

    #Basic information
    title = models.CharField(max_length=114, unique=True)
    short_description = models.TextField(max_length=255, null=True)
    slug = models.SlugField(unique=True, max_length=255)
    
    #Crossed Data
    location = models.ForeignKey(Location, related_name='Country Related')
 
    #Profile Content Information
    content = models.TextField(max_length=2000, null=True)
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
   
    def __unicode__(self):
        return '%s' % self.title



class CountryGallery(models.Model):
 	image = models.ImageField(upload_to='countries/')
	image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
	country = models.ForeignKey(Country)

