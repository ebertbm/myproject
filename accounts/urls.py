from django.conf.urls import patterns, url

from accounts.views import UserProfileEditView, ClientProfileEditView, InstitutionEditView
from accounts.api.views import StudentDetailAPI, StudentEnquiriesAPI
from accounts import views



from django.contrib.auth.decorators import login_required as auth #Prevent unlogged user to see this view


urlpatterns = patterns('',


     #CHOOSE STUDENT OR CLIENT VIEW
     url(r'^user/$', auth(views.accounts_view), name='user_profile'),


############### STUDENT URLS #########################
     #STUDENT API
     url(r'^user/profile/api/$', auth(StudentDetailAPI), name='student-detail-api'),
     url(r'^user/enquiries/api/$', auth(StudentEnquiriesAPI), name='student-enquiries-apo'),


     #STUDENT URLS
     url(r'^user/student_enquiries.html', auth(views.StudentEnquiriesView), name='student-enquiries'),
     url(r'^user/student_edit_profile.html', auth(UserProfileEditView.as_view()), name='student-edit-profile'),
     url(r'^user/enquiries/student_change_password.html', auth(views.StudentChangePasswordView), name='student-change-password'),



     #url(r'^editprofile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),



############### CLIENT URLS #########################


     #CLIENT ACCOUNT URLS
     url(r'^user/client/client_edit_profile.html', auth(ClientProfileEditView.as_view()), name="client_edit_profile"),
     url(r'^user/client/dashboard.html', auth(views.ClientDashboardView), name="dashboard_client"),
     url(r'^user/client/editinstitution/(?P<client>\d+)/$', auth(InstitutionEditView.as_view()), name="client_edit_institution"),
)






