from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from .forms import UserProfileForm, ClientProfileForm, InstitutionEditForm
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

from accounts.models import UserProfile, ClientProfile

from institution.models import Institution


#def index(request):
#	return render_to_response("index.html", RequestContext(request))


""""
class accounts_view(DetailView, request):
    if request.user.is_client(): # <-- check with your logic, is_student() is a stub
        return InstitutionProfileDetailView.as_view()
    else:
        return UserProfileDetailView.as_view()
    #elif request.user.is_institute():
"""""
"""
def account_view():
    client = self.is_client()
    if client:
        return "account/institution_profile.html"
    else:
        return "account/user_profile.html"
"""
"""
def accounts_view(request, slug):
    #currentuser= request.user.id
    clients = ClientProfile.objects.filter(user=request.user)
    if clients is None:
        return #UserProfileDetailView.as_view() 
    else:
        return #InstitutionProfileDetailView.as_view()
"""


class UserProfileDetailView(DetailView):
    model = UserProfile
    slug_field = "username"
    template_name = "account/student/user_profile.html"

    def get_object(self, queryset=None):
    	user = super(UserProfileDetailView, self).get_object(queryset)
    	UserProfile.objects.get_or_create(user=user)
    	return user



class UserProfileEditView(UpdateView):
	model = get_user_model()
	form_class = UserProfileForm
	template_name = "account/student/edit_profile.html"

	def get_object(self, queryset=None):
		return UserProfile.objects.get_or_create(user=self.request.user)[0]

	def get_success_url(self):
		return reverse("user_profile", kwargs={'slug': self.request.user})





#def get_institution():
 #   institutions = Institution.objects.filter(client=self.request.user)



def ClientProfileDetailView(request, slug):

    client = get_object_or_404(ClientProfile, user=request.user)
    institutions = Institution.objects.filter(client=client.id)
    return render_to_response("account/client/client_profile.html", locals(), context_instance=RequestContext(request))

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


