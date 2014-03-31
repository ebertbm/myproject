from django.db import models
from institution.models import Institution
from random import random



class Deal(models.Model):
	#Crossed data
	institution = models.ForeignKey(Institution, blank=True)

	#Deal Information
	title = models.CharField(max_length=114, blank=False)
	header = models.CharField(max_length=114, blank=False)
	thumbnail = models.FileField(upload_to='institutions/deals/', blank=True, null=True)
	slug = models.SlugField(unique=True, max_length=255)
	content = models.TextField(max_length=255, null=True)
	
	
	visibility_value = models.IntegerField(max_length=2, blank=True, null=True)

	
	#Tick boxes
	active = models.BooleanField(default=False)

	#Created date
	created = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return '%s' % format(self.title)






	def weighted_choice_sub(weights):
		rnd = random.random() * sum(weights)
		for i, w in enumerate(weights):
			rnd -= w
			if rnd < 0:
				return i

	
	def randomDeals(self):
		deals = self.objects.values_list('visibility_value', flat=True).order_by('id')
		choice = self.weighted_choice_sub(deals)
		return choice





	
