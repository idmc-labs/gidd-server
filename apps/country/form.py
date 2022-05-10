from django import forms
from apps.country.models import (
    OverView, Country
)
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE


class OverviewForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"))

    class Meta:
        model = OverView
        fields = '__all__'


class CountryForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"), required=False)
    essential_links = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Essential links"), required=False
    )
    contact_person_description = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Contact person description"), required=False
    )

    latest_new_displacements_description = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Latest new displacements description"), required=False
    )
    internal_displacement_description = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Internal displacement description"), required=False
    )

    class Meta:
        model = Country
        fields = '__all__'
