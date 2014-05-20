from django.conf.urls import patterns, url

from institution import views

from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

"""
sqs = SearchQuerySet().facet('type_institution').facet('levels').facet('languages').facet('location')


urlpatterns = patterns('haystack.views', 
	#url(r'^$', views.index, name='index'),
	url(r'^$', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
	url(r'^/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)"""

urlpatterns = patterns('', 
	#url(r'^$', views.index, name='index'),
	#url(r'^$',  views.search, name='haystack_search'),
	#url(r'^results',  views.results, name='results'),
	url(r'^(?P<pk>\d+)/$', views.DetailView, name='detail'),
	url(r'^(?P<pk>\d+)/photos/$',  views.PhotosView, name='institution_photos'),
	url(r'^(?P<pk>\d+)/videos/$',  views.VideosView, name='institution_videos'),
	url(r'^(?P<pk>\d+)/deals/$',  views.DealsView, name='institution_deals'),
	url(r'^(?P<pk>\d+)/map/$',  views.MapView, name='institution_map'),
	url(r'^(?P<pk>\d+)/street/$',  views.StreetView, name='institution_street'),

	url(r'^(?P<pk>\d+)/description/$',  views.DescriptionView, name='institution_description'),
	url(r'^(?P<pk>\d+)/studyareas/$',  views.StudyAreasView, name='institution_areas'),
	url(r'^(?P<pk>\d+)/studylevels/$',  views.StudyLevelsView, name='institution_levels'),
	url(r'^(?P<pk>\d+)/studentservices/$',  views.StudentServicesView, name='institution_services'),

)