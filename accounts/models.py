from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress

from variables.models import Location, StudyArea, StudyLevel, LanguageCourse


GENDERS_TYPES = (
    ('ma', 'Male'),
    ('fe', 'Female'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    about_me = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=40, choices=GENDERS_TYPES, blank=True)
    birth = models.DateTimeField(blank=True, null=True)
    
    #Contact Information
    location = models.ManyToManyField(Location, related_name='homecountry')
    address = models.CharField(max_length=254, blank=True)
    zipcode = models.CharField(max_length=56, blank=True)
    phone = models.CharField(max_length=56, blank=True)



    #Interested
    countries_interested = models.ManyToManyField(Location, blank=True, related_name='countries interested')
    areas_interested = models.ManyToManyField(StudyArea, blank=True)
    levels_interested = models.ManyToManyField(StudyLevel, blank=True)
    languages_interested= models.ManyToManyField(LanguageCourse, blank=True)

    def __unicode__(self):
        return '%s' % format(self.user)
       # return '%s %s %s %s %s %s %s %s %s %s %s %s' % (format(self.user.email), self.user, self.about_me, self.gender, self.birth, 
        #    self.location, self.address, self.zipcode, self.phone, self.countries_interested, self.levels_interested,
        #    self.languages_interested)

    #class Meta:
    #    db_table = 'user_profile'

    def get_user_email(self):
        if self.user.email:
            return self.user.email

    def get_user_id(self):
        return self.user


    def account_verified(self):
		if self.user.is_authenticated:
			result = EmailAddress.objects.filter(email=self.user.email)
			if len(result):
				return result[0].verified
				return False


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])




User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class ProductOrder(models.Model):
    name = models.CharField(max_length=114, unique=True)
    description = models.TextField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name


class ClientProfile(models.Model):
    user = models.OneToOneField(User, related_name='client')
    gender = models.CharField(max_length=40, choices=GENDERS_TYPES, blank=True)

    #Contact Information
    location = models.ManyToManyField(Location)
    address = models.CharField(max_length=254, blank=True)
    zipcode = models.CharField(max_length=56, blank=True)
    phone = models.CharField(max_length=56, blank=True)

    def __unicode__(self):
        return '%s' % format(self.user)
    


class ClientOrder(models.Model):
    product = models.ForeignKey(ProductOrder, blank=False)
    client = models.ForeignKey(ClientProfile, blank=False)
    time_length = models.IntegerField(max_length=2, blank=False)
    comments = models.TextField(max_length=255, blank=True)
    active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.id

