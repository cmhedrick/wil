import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.views.generic.edit import ModelFormMixin

from app_wil import models


class AddTardyForm(forms.Form):
    name = forms.CharField(
        widget = forms.TextInput(attrs={
            'placeholder': "Full Name"
        }),
        required = True
    )
    tardy_date = forms.DateField(
        widget = SelectDateWidget(
            years = range(datetime.date.today().year,1960,-1)),
        required = True
    )
    period = forms.CharField(
        widget = forms.Select(choices = models.Tardy.PERIOD_CHOICES),
        required = True
    )
    excuse = forms.CharField(
        widget = forms.Select(choices = models.Tardy.EXCUSE_CHOICES),
        required = True
    )
    note = forms.BooleanField(
        widget = forms.CheckboxInput(),
        required = False
    )
    other = forms.CharField(
        widget = forms.TextInput(attrs={
            'placeholder': "Other Excuse"
        }),
        required = False
    )
        
    def save(self):
        info = self.cleaned_data
        new_tardy = models.Tardy.objects.create(
            name = info['name'],
            tardy_datetime = info['tardy_date'],
            period = info['period'],
            excuse = info['excuse'],
            note = info['note']
        )
        new_tardy.save()

