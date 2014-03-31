from django import forms
from .models import UserProfile, ClientProfile
from institution.models import Institution

class UserProfileForm(forms.ModelForm):
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