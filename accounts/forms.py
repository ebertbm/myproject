from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, ClientProfile
from institution.models import Institution

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
		# magic end
		
		super(UserProfileForm, self).__init__(*args, **kwargs)
		
		self.fields.update(self.uf.fields)
		self.initial.update(self.uf.initial)
		
		# define fields order if needed
		self.fields.keyOrder = (
            'first_name',
			'last_name',
			'username',
			'email',
			'gender',
            'birth',
            'location',
            'address',
			'zipcode',
			'phone',
			'countries_interested',
            'areas_interested',
            'levels_interested',
			'languages_interested',
            'about_me',
        )
		
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