from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, ClientProfile
from institution.models import Institution
from variables.models import Location

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class UserProfileForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		# magic 
		self.user = kwargs['instance'].user
		user_kwargs = kwargs.copy()
		user_kwargs['instance'] = self.user
		self.uf = UserForm(*args, **user_kwargs)


		#CRISPY FORM
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-6'
		self.helper.layout = Layout(
			'first_name',
			'last_name',
			'email',
			Field('gender', css_class="col-lg-2"),
			'birth',
			'location',
			'address',
			'zipcode',
			'phone',
			#Field('birth', css_class='input-small' , readonly='readonly', id="data_end", template='util/datepicker_end.html'),
			'levels_interested',
			'areas_interested',
			'countries_interested',
			FormActions(
				Submit('save_changes', 'Save changes', css_class="btn-primary"),
				)
			)
		# magic end
		
		super(UserProfileForm, self).__init__(*args, **kwargs)

		self.fields["location"].widget = forms.widgets.Select()
		self.fields["location"].queryset = Location.objects.all()
		
		self.fields.update(self.uf.fields)
		self.initial.update(self.uf.initial)
		
		
	def save(self, *args, **kwargs):
		# save both forms   
		self.uf.save(*args, **kwargs)
		return super(UserProfileForm, self).save(*args, **kwargs)
		
	class Meta:
		model = UserProfile
		exclude = ('user',)





class ClientProfileForm(forms.ModelForm):	
    class Meta:
        model = ClientProfile
        exclude = ('user',)



class InstitutionEditForm(forms.ModelForm):
    class Meta:
        model = Institution
        exclude = ('client', 'is_premium', 'is_featured', 'active')