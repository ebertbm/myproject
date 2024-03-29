from django.views import generic
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext

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




def DetailView(request, pk):

    institution = get_object_or_404(Institution, id=pk)

    level_study = institution.level_study.values_list('name_level', flat=True).order_by('name_level')
    study_area = institution.study_area.values_list('name_area', flat=True).order_by('name_area')

    return render_to_response("institution/detail.html", locals(), 
        context_instance=RequestContext(request))


def PhotosView(request, pk):
    return render_to_response("institution/tabs/photos.html", locals(), 
        context_instance=RequestContext(request))

def VideosView(request, pk):
    return render_to_response("institution/tabs/videos.html", locals(), 
        context_instance=RequestContext(request))

def DealsView(request, pk):
    return render_to_response("institution/tabs/deals.html", locals(), 
        context_instance=RequestContext(request))

def DescriptionView(request, pk):
    institution = get_object_or_404(Institution, id=pk)
    return render_to_response("institution/tabs/description.html", locals(), 
        context_instance=RequestContext(request))

def StudyAreasView(request, pk):
    institution = get_object_or_404(Institution, id=pk)
    study_area = institution.study_area.values_list('name_area', flat=True).order_by('name_area')
    return render_to_response("institution/tabs/areas.html", locals(), 
        context_instance=RequestContext(request))

def StudyLevelsView(request, pk):
    institution = get_object_or_404(Institution, id=pk)
    level_study = institution.level_study.values_list('name_level', flat=True).order_by('name_level')
    return render_to_response("institution/tabs/levels.html", locals(), 
        context_instance=RequestContext(request))

def StudentServicesView(request, pk):
    return render_to_response("institution/tabs/services.html", locals(), 
        context_instance=RequestContext(request))

def MapView(request, pk):
    return render_to_response("institution/tabs/map.html", locals(), 
        context_instance=RequestContext(request))

def StreetView(request, pk):
    return render_to_response("institution/tabs/street.html", locals(), 
        context_instance=RequestContext(request))

