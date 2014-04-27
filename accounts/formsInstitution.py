from django import forms
from institution.models import Institution
from variables.models import Location

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions






class EditDetailsForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		#CRISPY FORM
		self.helper = FormHelper()
		self.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-6'
		#self.helper.add_input(Submit("submit", "Save", css_class="btn-primary"))
		self.helper.layout = Layout(
			'name_institution',
			'short_description',
			'content',
			Field('client', type="hidden"),
			Field('location', type="hidden"),
			Field('docfile', type="hidden"),
			Field('slug', type="hidden"),
			Field('address', type="hidden"),
			Field('contact_email', type="hidden"),
			Field('contact_website', type="hidden"),
			Field('phone', type="hidden"),
			Field('published', type="hidden"),
			Field('is_premium', type="hidden"),
			Field('is_featured', type="hidden"),
			Field('type_institution', type="hidden"),
			Field('level_study', type="hidden"),
			Field('course_language', type="hidden"),
			Field('study_area', type="hidden"),
			FormActions( Submit('submit', 'Save changes', css_class="btn-primary"))
			)

		super(EditDetailsForm, self).__init__(*args, **kwargs)
		#self.fields['client'].initial = self.instance.client

	class Meta:
		model = Institution
        exclude = ('created',)



class EditContactForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		#CRISPY FORM
		self.helper = FormHelper()
		self.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-6'
		#self.helper.add_input(Submit("submit", "Save", css_class="btn-primary"))
		self.helper.layout = Layout(
			'location',
			'address',
			'phone',
			'contact_email',
			'contact_website',
			Field('client', type="hidden"),
			Field('docfile', type="hidden"),
			Field('slug', type="hidden"),
			Field('published', type="hidden"),
			Field('is_premium', type="hidden"),
			Field('is_featured', type="hidden"),
			Field('type_institution', type="hidden"),
			Field('level_study', type="hidden"),
			Field('course_language', type="hidden"),
			Field('study_area', type="hidden"),
			Field('name_institution', type="hidden"),
			Field('short_description', type="hidden"),
			Field('content', type="hidden"),
			FormActions( Submit('submit', 'Save changes', css_class="btn-primary"))
			)

		super(EditContactForm, self).__init__(*args, **kwargs)
		#self.fields['client'].initial = self.instance.client

	class Meta:
		model = Institution
        exclude = ('created',)





class EditAcademicForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		#CRISPY FORM
		self.helper = FormHelper()
		self.form_method = 'post'
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-6'
		#self.helper.add_input(Submit("submit", "Save", css_class="btn-primary"))
		self.helper.layout = Layout(
			'favorite_colors',
			'type_institution',
			'level_study',
			'study_area',
			'course_language',
			Field('client', type="hidden"),
			Field('location', type="hidden"),
			Field('docfile', type="hidden"),
			Field('slug', type="hidden"),
			Field('address', type="hidden"),
			Field('contact_email', type="hidden"),
			Field('contact_website', type="hidden"),
			Field('phone', type="hidden"),
			Field('published', type="hidden"),
			Field('is_premium', type="hidden"),
			Field('is_featured', type="hidden"),
			Field('type_institution', type="hidden"),
			Field('level_study', type="hidden"),
			Field('course_language', type="hidden"),
			Field('study_area', type="hidden"),
			Field('name_institution', type="hidden"),
			Field('short_description', type="hidden"),
			Field('content', type="hidden"),
			FormActions( Submit('submit', 'Save changes', css_class="btn-primary"))
		)

		super(EditAcademicForm, self).__init__(*args, **kwargs)
		#self.fields['client'].initial = self.instance.client

	class Meta:
		model = Institution
        exclude = ('created',)


	FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))

	favorite_colors = forms.MultipleChoiceField(required=False,
    	 widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)








