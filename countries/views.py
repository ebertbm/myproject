from django.views import generic
from countries.models import Country

# Create your views here.



         


class CountriesView(generic.ListView):
    template_name = 'countries/allcountries.html'
    context_object_name = 'latest_deal_list'

    def get_queryset(self):
        """Return the last five published deals."""
        return Country.objects.order_by('-created')



class DetailView(generic.DetailView):
    model = Country
    template_name = 'countries/detail.html'