from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class LatchPairForm(forms.Form):
	latch_pin = forms.CharField()

class LatchSetupForm(ModelForm):
	class Meta:
		model = LatchSetup
	#latch_appid = form.CharField()
	#latch_secret = form.CharField()

class LatchUnpairForm(forms.Form):
	latch_confirm = forms.BooleanField()
