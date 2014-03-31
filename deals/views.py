from django.views import generic
from deals.models import Deal
from random import sample




"""
def weighted_choice_sub(weights):
	rnd = random.random() * sum(weights)
	for i, w in enumerate(weights):
		rnd -= w
		if rnd < 0:
			return i


def randomDeals(num_deal_displayed):
	deals = Deal.objects.values_list('visibility_value', flat=True).order_by('id')
	
	for i in num_deal_displayed:


	choice = Deal.objects.filter(id=weighted_choice_sub(deals)+1)
	return choice

"""


def randomDeals():
	count = Deal.objects.all().count()
	rand_ids = sample(xrange(1, count+1), 3)
	return Deal.objects.filter(id__in=rand_ids)


class IndexView(generic.ListView):
    template_name = 'institution/deals/index.html'
    context_object_name = 'latest_deal_list'

    def get_queryset(self):
        """Return the last five published deals."""
        return randomDeals()
        #Deal.objects.order_by('-created')[:3]



class AllDealsView(generic.ListView):
    template_name = 'institution/deals/alldeals.html'
    context_object_name = 'latest_deal_list'

    def get_queryset(self):
        """Return the last five published deals."""
        return Deal.objects.order_by('-created')



class DetailView(generic.DetailView):
    model = Deal
    template_name = 'institution/deals/detail.html'