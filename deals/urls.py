from django.conf.urls import patterns, url

from deals import views


urlpatterns = patterns('', 
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^alldeals/$', views.AllDealsView.as_view(), name='alldeals'),
	url(r'^(?P<slug>[\w\-]+)/$', views.DetailView.as_view(), name='deal_detail'),
)

