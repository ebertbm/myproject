from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from django.contrib.auth.models import User

from accounts.models import UserProfile, ClientProfile
from institution.models import Institution
from requestforms.models import Enquiry

from .forms import UserProfileForm, ClientProfileForm, InstitutionEditForm



def accounts_view(request, slug):
    clients = ClientProfile.objects.filter(user=request.user)

    if clients:
        return ClientProfileDetailView(request, slug) 
    else:
        return UserProfileDetailView(request, slug)
         


def UserProfileDetailView(request, slug):
    student = get_object_or_404(UserProfile, user=request.user)
    enquiries = Enquiry.objects.filter(student=student)


    return render_to_response("account/student/student_profile.html", locals(), 
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
    template_name = "account/student/edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("user_profile", kwargs={'slug': self.request.user})



def ClientProfileDetailView(request, slug):

    client = get_object_or_404(ClientProfile, user=request.user)
    institutions = Institution.objects.filter(client=client.id)
    enquiries = Enquiry.objects.filter(client=client)

    return render_to_response("account/client/client_profile.html", locals(), 
        context_instance=RequestContext(request))

"""   def get_object(self, queryset=None):
        user = super(ClientProfileDetailView, self).get_object(queryset)
        ClientProfile.objects.get_or_create(user=user)
        return user
"""

class ClientProfileEditView(UpdateView):
    model = get_user_model()
    form_class = ClientProfileForm
    template_name = "account/client/client_edit_profile.html"

    def get_object(self, queryset=None):
        return ClientProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("client_profile", kwargs={'slug': self.request.user})



class InstitutionEditView(UpdateView):
    model = Institution
    form_class = InstitutionEditForm
    template_name = "account/client/institution_edit.html"

    def get_object(self, queryset=None):
        return Institution.objects.get_or_create(client=self.kwargs['client'])[0]

    def get_success_url(self):
        return reverse("client_profile", kwargs={'slug': self.request.user})