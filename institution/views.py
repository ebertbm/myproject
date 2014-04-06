from django.views import generic
from django.shortcuts import render, render_to_response

from institution.models import Institution
from institution.forms import InstitutionSearchForm

from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView



class InstitutionSearchView(FacetedSearchView):
    __name__ = 'InstitutionSearchView'
    template = 'search/search.html'
     
    def __init__(self, *args, **kwargs):
        # Needed to switch out the default form class.
        if kwargs.get('form_class') is None:
            kwargs['form_class'] = InstitutionSearchForm
         
        super(InstitutionSearchView, self).__init__(*args, **kwargs)

class InstitutionResultsView(FacetedSearchView):
    __name__ = 'InstitutionSearchView'
    template = 'search/results.html'
     
    def __init__(self, *args, **kwargs):
        # Needed to switch out the default form class.
        if kwargs.get('form_class') is None:
            kwargs['form_class'] = InstitutionSearchForm
         
        super(InstitutionResultsView, self).__init__(*args, **kwargs)

  
def search(request):
    sqs = SearchQuerySet().facet('type_institution').facet('levels').facet('languages').facet('location')
    form = InstitutionSearchForm(request.GET)
    if form.is_valid():
        form.cleaned_data
 
    return InstitutionSearchView(form_class=InstitutionSearchForm, searchqueryset=sqs)(request)


#MACHETAZO.... HAY QUE OPTIMIZAR!
def results(request):
    sqs = SearchQuerySet().facet('type_institution').facet('levels').facet('languages').facet('location')
    form = InstitutionSearchForm(request.GET)
    if form.is_valid():
        form.cleaned_data

 
    print "results"
    return InstitutionResultsView(form_class=InstitutionSearchForm, searchqueryset=sqs)(request)


class DetailView(generic.DetailView):
    model = Institution
    template_name = 'institution/detail.html'