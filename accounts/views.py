from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from accounts.models import UserProfile, ClientProfile
from institution.models import Institution
from requestforms.models import Enquiry

from .forms import UserProfileForm, ClientProfileForm
from .formsInstitution import EditDetailsForm, EditAcademicForm, EditContactForm



def accounts_view(request):
    clients = ClientProfile.objects.filter(user=request.user)

    if clients:
        return ClientProfileDetailView(request) 
    else:
        return UserProfileDetailView(request)




##########################STUDENT VIEWS###########################

def UserProfileDetailView(request):
    return render_to_response("account/student/student_profile.html", locals(), 
        context_instance=RequestContext(request))


def StudentEnquiriesView(request):
    return render_to_response("account/student/student_enquiries.html", locals(), 
        context_instance=RequestContext(request))

def StudentEditProfileView(request):
    return render_to_response("account/student/student_edit_profile.html", locals(), 
        context_instance=RequestContext(request))

def StudentChangePasswordView(request):
    return render_to_response("account/student/student_change_password.html", locals(), 
        context_instance=RequestContext(request))
"""    
slug_field = "username"
def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user
        
    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context['enquiries'] = Enquiry.objects.filter(email=self.request.user.email)
        return context
"""


class UserProfileEditView(UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = "account/student/student_edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("student-edit-profile")






##########################CLIENT VIEWS###########################

def ClientProfileDetailView(request):

    client = get_object_or_404(ClientProfile, user=request.user)
    institutions = Institution.objects.filter(client=client.id)[0]
    enquiries = Enquiry.objects.filter(client=client)

    return render_to_response("account/client/client_profile.html", locals(), 
        context_instance=RequestContext(request))

"""   def get_object(self, queryset=None):
        user = super(ClientProfileDetailView, self).get_object(queryset)
        ClientProfile.objects.get_or_create(user=user)
        return user
"""



def ClientDashboardView(request):
    return render_to_response("account/client/dashboard.html", locals(), 
        context_instance=RequestContext(request))


class ClientProfileEditView(UpdateView):
    model = get_user_model()
    form_class = ClientProfileForm
    template_name = "account/client/client_edit_profile.html"

    def get_object(self, queryset=None):
        return ClientProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("client_edit_profile")


def ClientLeadsView(request):
    return render_to_response("account/client/leads.html", locals(), 
        context_instance=RequestContext(request))


def AngularRouterView(request):
    return render_to_response("account/client/router.html", locals(), 
        context_instance=RequestContext(request))


def InstitutionView(request):
    client = get_object_or_404(ClientProfile, user=request.user)
    institution = Institution.objects.get_or_create(client=client.id)[0]

    return render_to_response("account/client/institution_profile.html", locals(), 
        context_instance=RequestContext(request))



def InstitutionDetailView(request):
    client = get_object_or_404(ClientProfile, user=request.user)
    institution = Institution.objects.get_or_create(client=client.id)[0]

    if request.method == 'POST':

        form = EditDetailsForm(request.POST, instance = institution)
        if form.is_valid():
            form.save()

            return  render_to_response('account/client/details.html', 
                {'form': form, 'institution':institution}, context_instance=RequestContext(request))
    else:
        form = EditDetailsForm(instance = institution)

    return render_to_response('account/client/details.html', 
        {'form': form, 'institution':institution}, context_instance=RequestContext(request))



def InstitutionContactView(request):
    client = get_object_or_404(ClientProfile, user=request.user)
    institution = Institution.objects.get_or_create(client=client.id)[0]

    if request.method == 'POST':

        form = EditContactForm(request.POST, instance = institution)
        if form.is_valid():
            form.save()

            return  render_to_response('account/client/contact_details.html', 
                {'form': form, 'institution':institution}, context_instance=RequestContext(request))
    else:
        form = EditContactForm(instance = institution)

    return render_to_response('account/client/contact_details.html', 
        {'form': form, 'institution':institution}, context_instance=RequestContext(request))





def InstitutionAcademicView(request):
    client = get_object_or_404(ClientProfile, user=request.user)
    institution = Institution.objects.get_or_create(client=client.id)[0]

    if request.method == 'POST':

        form = EditAcademicForm(request.POST, instance = institution)
        if form.is_valid():
            form.save()

            return  render_to_response('account/client/academic_details.html', 
                {'form': form, 'institution':institution}, context_instance=RequestContext(request))
    else:
        form = EditAcademicForm(instance = institution)

    return render_to_response('account/client/academic_details.html', 
        {'form': form, 'institution':institution}, context_instance=RequestContext(request))

