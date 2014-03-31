from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views import generic

from institution.models import Institution



def index(request):
	return render_to_response("search/search.html", RequestContext(request))

class DetailView(generic.DetailView):
    model = Institution
    template_name = 'institution/detail.html'

