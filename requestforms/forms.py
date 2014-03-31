from django import forms
from requestforms.models  import Enquiry
from institution.models import Institution
from variables.models import StudyArea, StudyLevel
from countries.models import Country

class EnquiryForm(forms.ModelForm):

	"""client = forms.ModelChoiceField(queryset = ClientProfile.objects.none(), empty_label=None, 
		widget=forms.HiddenInput())"""
	study_level_interested = forms.ModelChoiceField(queryset = StudyLevel.objects.values_list('id', flat=True))
	area_interested = forms.ModelChoiceField(queryset = StudyArea.objects.values_list('id', flat=True))


	def get_study_levels(self, schools):
		study_levels = schools.level_study.values_list('id', flat=True).order_by('name_level')
		return study_levels

	def get_study_areas(self, schools):
		study_areas = schools.study_area.values_list('id', flat=True).order_by('name_area')
		return study_areas

	def __init__(self, institution_id, *args, **kwargs):
		super(EnquiryForm, self).__init__(*args, **kwargs)
		schools = Institution.objects.get(id=institution_id)
		self.fields['study_level_interested'].queryset = self.get_study_levels(schools)
		self.fields['area_interested'].queryset = self.get_study_areas(schools)
		#self.fields['client'].queryset = self.get_client(institution_id)

	class Meta:
		model = Enquiry
		exclude = ('student', 'client')




class EnquiryCountryForm(forms.ModelForm):


	INSTITUTION_TYPES = (
		('bs', 'Business School'),
		('cc', 'Community College'),
		('hs', 'High School'),
		('ls','Language School'),
		('pc', 'Private College'),
		('sc', 'Summer Camp'),
		('un', 'University')
		)


	institution_type = forms.ChoiceField(label="Institution Type", choices = INSTITUTION_TYPES)


	def get_institutions_country(self, location_id):
		institutions = Institution.objects.filter(location__id = location_id)
		return institutions


	def __init__(self, location_id, *args, **kwargs):
		super(EnquiryCountryForm, self).__init__(*args, **kwargs)

		self.fields["institution_interested"].widget = forms.widgets.CheckboxSelectMultiple()
		self.fields["institution_interested"].queryset = self.get_institutions_country(location_id)

		self.fields["study_level_interested"].widget = forms.widgets.CheckboxSelectMultiple()
		self.fields["study_level_interested"].queryset = StudyLevel.objects.all()
		
		self.fields["area_interested"].widget = forms.widgets.CheckboxSelectMultiple()
		self.fields["area_interested"].queryset = StudyArea.objects.all()
 
		#self.fields['client'].queryset = self.get_client(institution_id)

	class Meta:
		model = Enquiry
		exclude = ('student', 'client', 'country_interested', 'enquiry_type')