from django.conf.urls import patterns, url

from accounts.views import UserProfileEditView, ClientProfileEditView, InstitutionAcademicView, InstitutionView
from accounts.api.studentAPI import StudentDetailAPI, StudentEnquiriesAPI
from accounts.api.institutionAPI import InstitutionEnquiriesAPI
from accounts import views



from django.contrib.auth.decorators import login_required as auth #Prevent unlogged user to see this view


urlpatterns = patterns('',


     #CHOOSE STUDENT OR CLIENT VIEW
     url(r'^user/$', auth(views.accounts_view), name='user_profile'),


#################### STUDENT URLS #########################
     #STUDENT API
     url(r'^user/profile/api/$', auth(StudentDetailAPI), name='student-detail-api'),
     url(r'^user/enquiries/api/$', auth(StudentEnquiriesAPI), name='student-enquiries-apo'),


     #STUDENT URLS
     url(r'^user/student_enquiries.html', auth(views.StudentEnquiriesView), name='student-enquiries'),
     url(r'^user/student_edit_profile.html', auth(UserProfileEditView.as_view()), name='student-edit-profile'),
     url(r'^user/enquiries/student_change_password.html', auth(views.StudentChangePasswordView), name='student-change-password'),



     #url(r'^editprofile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),



#################### CLIENT URLS #########################

     #Institution API
     url(r'^user/institution_enquiries/api/$', auth(InstitutionEnquiriesAPI), name='institution_enquiries_api'),

     #CLIENT ACCOUNT URLS
     url(r'^user/client/client_edit_profile.html', auth(ClientProfileEditView.as_view()), name="client_edit_profile"),
     url(r'^user/client/dashboard.html', auth(views.ClientDashboardView), name="dashboard_client"),
     url(r'^user/client/leads.html', auth(views.ClientLeadsView), name="institution_leads"),
     url(r'^user/client/institution/$', auth(views.InstitutionView), name="client_profile_institution"),

     #INSTITUTION MENU URLS
     url(r'^user/client/router.html', auth(views.AngularRouterView), name="router_client_angular"),
     
     url(r'^user/client/details.html', auth(views.InstitutionDetailView), name="institution_edit_details"),
     url(r'^user/client/contact_details.html', auth(views.InstitutionContactView), name="institution_edit_contact"),
     url(r'^user/client/academic_details.html', auth(views.InstitutionAcademicView), name="institution_edit_academic"),
     url(r'^user/client/photos.html', auth(views.AngularRouterView), name="institution_photos"),
     url(r'^user/client/videos.html', auth(views.AngularRouterView), name="institution_videos"),



)






