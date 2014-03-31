from django.conf.urls import patterns, url

from countries import views


urlpatterns = patterns('', 
	url(r'^$', views.CountriesView.as_view(), name='index'),
	url(r'^(?P<slug>[\w\-]+)/$', views.DetailView.as_view(), name='country_detail'),
)


