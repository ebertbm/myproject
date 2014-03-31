from django.conf.urls import patterns, url

from requestforms import views

urlpatterns = patterns('', 
	url(r'^(?P<institution_id>\d+)/$', views.enquiryInstitution, name='enquiry_form'),
	url(r'^country/(?P<country_id>\d+)/$', views.enquiryCountry, name='enquiry_country_form'),

)


