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
	url(r'^$',  views.search, name='haystack_search'),
	url(r'^results',  views.results, name='results'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)