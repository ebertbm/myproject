from django.conf.urls import patterns, url

from accounts.views import UserProfileDetailView, UserProfileEditView, ClientProfileEditView, InstitutionEditView, accounts_view
from accounts import views
#, accounts_view

from django.contrib.auth.decorators import login_required as auth #Prevent unlogged user to see this view







urlpatterns = patterns('',
	# url(r'^user/(?P<slug>\w+)/$', accounts_view.as_view(), name='user_profile'),
     #url(r'^user/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name='user_profile'),
     url(r'^user/(?P<slug>\w+)/$', auth(views.accounts_view), name='user_profile'),
     url(r'^editprofile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),

     #url(r'^client/(?P<slug>\w+)/$', views.ClientProfileDetailView, name='client_profile'),
     url(r'^editaccount/$', auth(ClientProfileEditView.as_view()), name="client_edit_profile"),

     url(r'^client/editinstitution/(?P<client>\d+)/$', auth(InstitutionEditView.as_view()), name="client_edit_institution"),



)