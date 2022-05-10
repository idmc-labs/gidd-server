from django import forms
from apps.good_practice.models import (
    Faq, MediaAndResourceLink, GoodPractice
)
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE


class FaqForm(forms.ModelForm):
    answer = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Answer"), required=False)

    class Meta:
        model = Faq
        fields = '__all__'


class MediaAndResourceLinkForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"), required=False)

    class Meta:
        model = MediaAndResourceLink
        fields = '__all__'


class GoodPracticeForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"), required=False)

    class Meta:
        model = GoodPractice
        fields = '__all__'
