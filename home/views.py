from django.shortcuts import render_to_response
from django.template import RequestContext


from deals.views import randomDeals

from countries.models import Country


def index(request):
	latest_deal_list = randomDeals()
	countries = Country.objects.order_by('-created')[:3]


	return render_to_response("index.html", locals(),
    	context_instance=RequestContext(request))