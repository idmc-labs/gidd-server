from django import forms
from apps.common.models import StaticPage
from tinymce.widgets import TinyMCE


class StaticPageForm(forms.ModelForm):
    class Meta:
        model = StaticPage
        fields = '__all__'
        widgets = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
