from django import forms
from basic.models import *
from django.contrib.auth.models import User

class ToySaveForm(forms.ModelForm):
    
    class Meta:
        model = Toy
