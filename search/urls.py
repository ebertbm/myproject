from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
	(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	url(r'^', include('institution.urls', namespace="institution")),
	#url(r'^', include('accounts.urls')),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^contact/', include('requestforms.urls', namespace="contacts")),
	url(r'^deal/', include('deals.urls', namespace="deals")),
	url(r'^country/', include('countries.urls', namespace="countries")),
	
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)