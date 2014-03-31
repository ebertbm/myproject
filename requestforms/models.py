from django.db import models
from accounts.models import UserProfile, ClientProfile
from variables.models import Location, StudyLevel, StudyArea
from institution.models import Institution
# Create your models here.

GENDERS_TYPES = (
    ('ma', 'Male'),
    ('fe', 'Female'),
)

ENQUIRY_TYPES = (
    ('01', 'Type A'),
    ('02', 'Type B'),
)

PLANNED_TIME = (
    ('01', '1-3 Months'),
    ('02', '3-6 Months'),
    ('03', '6-12 Months'),
    ('04', 'More thna 12 Months'),
)




class Enquiry(models.Model):
	#Crossed data
	student = models.ForeignKey(UserProfile, null=True, blank=True, default = None)
	client = models.ForeignKey(ClientProfile , null=True, blank=True, default = None)

	#Enquiry Type
	enquiry_type = models.CharField(max_length=2, choices=ENQUIRY_TYPES, blank=True)

    #Basic Information 
	first_name = models.CharField(max_length=114, blank=False)
	last_name = models.CharField(max_length=114, blank=False)
	gender = models.CharField(max_length=40, choices=GENDERS_TYPES, blank=False)

	#Country Interested
	country_interested = models.ForeignKey(Location, related_name='Country_Interested', null=True, blank=True, default = None)
	
	#Contact Information
	email = models.EmailField(blank=False)
	country = models.ForeignKey(Location)
	address = models.CharField(max_length=254, blank=True, null=True)
	zipcode = models.CharField(max_length=56, blank=True)
	phone = models.IntegerField(max_length=10, blank=False)

	#Enquery Content Information
	content = models.TextField(max_length=2000, null=True)


	#Study Data
	expected_time = models.CharField(max_length=40, choices=PLANNED_TIME, null=False)
	more_info = models.CharField(max_length=60, blank=True)
	study_level_interested = models.ManyToManyField(StudyLevel, blank=True)
	area_interested = models.ManyToManyField(StudyArea, blank=True)
	institution_interested = models.ManyToManyField(Institution, blank=True)

	#Tick boxes
	suscribed = models.BooleanField(default=True)

	#Created date
	created = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return '%s' % format(self.email)
"""		
	def get_study_level(self, institution_id):
		institution = Institution.objects.get(id=institution_id)
		study_levels = institution.objects.values_list('level_study', flat=True).order_by('level_study')
		
		return study_levels """