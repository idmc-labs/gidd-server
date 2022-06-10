from django import forms
from apps.common.models import StaticPage
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE


class StaticPageForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"), required=False)

    class Meta:
        model = StaticPage
        fields = '__all__'
