from django import forms
import re
from apps.good_practice.models import (
    Faq, GoodPractice, Gallery
)
from django.utils.translation import ugettext_lazy as _
from tinymce.widgets import TinyMCE
from django.forms import ValidationError


class FaqForm(forms.ModelForm):
    answer = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Answer"), required=False)

    class Meta:
        model = Faq
        fields = '__all__'


class GoodPracticeForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_("Description"), required=False)
    media_and_resource_links = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), label=_("Media and resource links"), required=False
    )

    class Meta:
        model = GoodPractice
        fields = '__all__'


class GalleryForm(forms.ModelForm):
    caption = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}), label=_("Caption"), required=False)

    class Meta:
        model = Gallery
        fields = '__all__'

    def clean_youtube_video_url(self):
        youtube_url = self.cleaned_data['youtube_video_url']
        if youtube_url:
            if re.search('^https://www.youtube.com/embed/.*', youtube_url) is None:
                raise ValidationError(_(
                    "Please provide valid embeddable youtube url."
                ))
        return self.cleaned_data['youtube_video_url']
