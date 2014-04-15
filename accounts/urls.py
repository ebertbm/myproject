from django.conf.urls import patterns, url

from accounts.views import UserProfileEditView, ClientProfileEditView, InstitutionEditView
from accounts import views


from django.contrib.auth.decorators import login_required as auth #Prevent unlogged user to see this view


urlpatterns = patterns('',


     #STUDENT ACCOUNT URLS
     url(r'^user/$', auth(views.accounts_view), name='user_profile'),
     url(r'^user/profile/api/$', auth(views.StudentDetailAPI), name='student-detail-api'),
     url(r'^user/enquiries/api/$', auth(views.StudentEnquiriesAPI), name='student-enquiries-apo'),

     url(r'^user/student_enquiries.html', auth(views.StudentEnquiriesView), name='student-enquiries'),
     url(r'^user/student_edit_profile.html', auth(views.StudentEditProfileView), name='student-edit-profile'),
     url(r'^user/enquiries/student_change_password.html', auth(views.StudentChangePasswordView), name='student-change-password'),






     url(r'^editprofile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),

     #CLIENT ACCOUNT URLS
     url(r'^editaccount/$', auth(ClientProfileEditView.as_view()), name="client_edit_profile"),
     url(r'^client/editinstitution/(?P<client>\d+)/$', auth(InstitutionEditView.as_view()), name="client_edit_institution"),



)

