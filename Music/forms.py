
from django.forms.widgets import HiddenInput, CheckboxSelectMultiple
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
        widgets = {
            'user': HiddenInput()
        }

