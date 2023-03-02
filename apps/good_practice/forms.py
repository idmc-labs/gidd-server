from django import forms
import re
from apps.good_practice.models import Faq, GoodPractice, Gallery
from django.utils.translation import gettext_lazy as _
from tinymce.widgets import TinyMCE
from django.forms import ValidationError


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = "__all__"
        widgets = {
            "answer": TinyMCE(attrs={"cols": 80, "rows": 30}),
        }


class GoodPracticeForm(forms.ModelForm):
    class Meta:
        model = GoodPractice
        fields = "__all__"
        widgets = {
            "description": TinyMCE(attrs={"cols": 80, "rows": 30}),
            "media_and_resource_links": TinyMCE(attrs={"cols": 80, "rows": 30}),
            "what_makes_this_promising_practice": TinyMCE(
                attrs={"cols": 80, "rows": 30}
            ),
            "description_of_key_lessons_learned": TinyMCE(
                attrs={"cols": 80, "rows": 30}
            ),
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"
        widgets = {
            "caption": TinyMCE(attrs={"cols": 80, "rows": 30}),
        }

    def clean_youtube_video_url(self):
        youtube_url = self.cleaned_data["youtube_video_url"]
        if youtube_url:
            if re.search("^https://www.youtube.com/embed/.*", youtube_url) is None:
                raise ValidationError(_("Please provide valid embeddable youtube url."))
        return self.cleaned_data["youtube_video_url"]
