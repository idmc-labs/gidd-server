from django import forms
from apps.country.models import (
    OverView, EssentialLink, ContactPerson, Country
)
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE


class OverviewForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"))

    class Meta:
        model = OverView
        fields = '__all__'


class EssentialLinkForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"))

    class Meta:
        model = EssentialLink
        fields = '__all__'


class ContactPersonFrom(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"))

    class Meta:
        model = ContactPerson
        fields = '__all__'


class CountryForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"))

    class Meta:
        model = Country
        fields = '__all__'
