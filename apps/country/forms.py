from django import forms
from apps.country.models import (
    OverView,
    Country,
)
from django.utils.translation import gettext_lazy as _
from tinymce.widgets import TinyMCE


class OverviewForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"))

    class Meta:
        model = OverView
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        overview_qs = OverView.objects.filter(country=cleaned_data['country'], year=cleaned_data['year'])
        if self.instance:
            overview_qs = overview_qs.exclude(pk=self.instance.pk)
        if overview_qs.exists():
            raise forms.ValidationError("Overview for this year already exists")
        else:
            return cleaned_data


class CountryForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"), required=False)
    essential_links = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Essential links"), required=False
    )
    contact_person_description = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Contact person description"), required=False
    )
    internal_displacement_description = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Internal displacement description"), required=False
    )
    displacement_data_description = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Displacement data description"), required=False
    )

    class Meta:
        model = Country
        fields = '__all__'
