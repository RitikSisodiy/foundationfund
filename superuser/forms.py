from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import about


def GenForm(Model,listHiddenfield=[]):
    data = {field:forms.HiddenInput() for field in listHiddenfield}
    class newform(forms.ModelForm):
        class Meta:
            model = Model
            exclude = ('id',)
            widgets = data
    return newform