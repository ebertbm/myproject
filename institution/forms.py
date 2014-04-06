
from django import forms

import haystack
from haystack.query import SearchQuerySet
from haystack.forms import SearchForm, FacetedSearchForm
 

 
class InstitutionSearchForm(FacetedSearchForm):
    #q is the default field in all SearchForm classes
    q = forms.CharField(required=False, label='Search') 
    #field1 = forms.ChoiceField(choices=INSTITUTION_TYPES, label='Search In')
 
    def no_query_found(self):
        return self.searchqueryset.all()

    def __init__(self, *args, **kwargs):
        super(InstitutionSearchForm, self).__init__(*args, **kwargs)
        #I usually put here the dynamic choices for my ChoiceFields
 
    def search(self):
        """Customize your search behavior here."""
        #call the search method by the superclass to narrow the search
        #but can be modified to set all rows for searching
        sqs = super(InstitutionSearchForm, self).search()

        # if something goes wrong
        if not self.is_valid():
            return self.no_query_found()
 
        
        return sqs