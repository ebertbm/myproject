from django.db import models
from accounts.models import ClientProfile
from variables.models import Location, StudyLevel, LanguageCourse, StudyArea


INSTITUTION_TYPES = (
    ('bs', 'Business School'),
    ('cc', 'Community College'),
    ('hs', 'High School'),
    ('ls','Language School'),
    ('pc', 'Private College'),
    ('sc', 'Summer Camp'),
    ('un', 'University')
)

class Institution(models.Model):

    client = models.ForeignKey(ClientProfile)
    #Basic information
    name_institution = models.CharField(max_length=114, unique=True, blank=True, null=True)
    docfile = models.FileField(upload_to='profiles/', blank=True, null=True)
    short_description = models.TextField(max_length=255, null=True)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    
    #Contact Information
    location = models.ForeignKey(Location)
    address = models.CharField(max_length=254, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_website = models.CharField(max_length=255, blank=True)
    phone = models.IntegerField(max_length=10, blank=True, null=True)
    
    #Profile Content Information
    content = models.TextField(max_length=2000, null=True)
    published = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    #Crossed Data
    type_institution = models.CharField(max_length=40, choices=INSTITUTION_TYPES, blank=True, null=True)
    level_study = models.ManyToManyField(StudyLevel, blank=True, null=True)
    course_language = models.ManyToManyField(LanguageCourse, blank=True, null=True)
    study_area = models.ManyToManyField(StudyArea, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-name_institution']


        """ def __unicode__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.client, self.name_institution, self.address, self.location, self.slug, self.contact_email, 
        self.contact_website, self.short_description, self.content, self.published, self.is_premium, 
        self.is_featured, self.created, self.type_institution, self.level_study, self.study_area, self.course_language)"""



    def __unicode__(self):
        return '%s' % self.name_institution

    def get_contact_email(self):
    	if self.contact_email:
    		return self.contact_email

    def get_institution_client(self):
        if self.client:
            return self.client.get
