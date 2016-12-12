'''
import floppyforms as forms
'''
from django import forms
import datetime
from core.models import activitiesMade, UserProfile

class activitiesMade(forms.ModelForm):
	class Meta:
		model = activitiesMade
		fields = '__all__'

class saveProfile(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'
