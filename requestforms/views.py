from django.shortcuts import render
from .forms import EnquiryForm, EnquiryCountryForm
from django.shortcuts import render, get_object_or_404, render_to_response
from institution.models import Institution
from django.template import RequestContext

from countries.models import Country
from variables.models import Location

# Create your views here.



def enquiryInstitution(request, institution_id):


        institution = get_object_or_404(Institution, id=institution_id)

        if request.POST:
            form = EnquiryForm(institution_id, request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.client = institution.client
                contact.enquiry_type = '01'
                contact.institution_interested = institution
                contact.country_interested = institution.location
                contact.save()

                return  render_to_response('forms/success.html', 
                    {'institution':institution}, context_instance=RequestContext(request))
        else:
            form = EnquiryForm(institution_id)

        return render_to_response('forms/enquiry_form.html', 
                                  {'form': form, 'institution':institution}, context_instance=RequestContext(request))



def enquiryCountry(request, country_id):

        country = get_object_or_404(Country, id=country_id)
        location_id = country.location.id

        if request.POST:
            form = EnquiryCountryForm(location_id, request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.country_interested = country.location
                contact.enquiry_type = '02'
                contact.save()
                #contact.save_m2m()

                return render_to_response('forms/success_country.html', 
                                  {'country':country}, context_instance=RequestContext(request))
        else:
            form = EnquiryCountryForm(location_id)

        return render_to_response('forms/enquiry_form_country.html', 
                                  {'form': form, 'country':country}, context_instance=RequestContext(request))
